# pylint: disable=no-member
# Pylint does not recognize pygame for some reason

import sys

import pygame

from game.game_logic import GameLogic
from game.top_score import TopScore
from game_config import GameConfig
from ui.board_ui import BoardUI

def draw_text(text, font, color, surface, pos):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(pos[0],pos[1]))
    surface.blit(textobj, textrect)

def button(data):
    color = data["hover_color"] if data["rect"].collidepoint(data["mouse"]) else data["base_color"]
    pygame.draw.rect(data["screen"], color, data["rect"], border_radius=10)
    pos = (data["rect"].centerx, data["rect"].centery)
    draw_text(data["text"], data["font"], data["text_color"],
       data["screen"], pos)
    return data["rect"].collidepoint(data["mouse"]) and data["click"]

def start_menu():
    # Check if the data for top score exits, if not make it
    TopScore().file_exists()
    pygame.init()
    config = GameConfig()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("2048")

    title_font = pygame.font.SysFont("arial", 72)
    button_font = pygame.font.SysFont("arial", 36)

    start_button = pygame.Rect(config.WIDTH // 2 - 100, config.HEIGHT // 2, 200, 60)
    quit_button = pygame.Rect(config.WIDTH // 2 -100, config.HEIGHT // 2 + 80, 200, 60)

    clock = pygame.time.Clock()

    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        mouse_pos = pygame.mouse.get_pos()
        screen.fill(config.BG_COLOR)

        pos = (config.WIDTH // 2, config.HEIGHT // 3)
        draw_text("2048", title_font, (119,110,101), screen, pos)

        start_button_data = {"rect": start_button,
            "text": "Start Game",
            "font": button_font,
            "screen": screen,
            "mouse": mouse_pos,
            "click": click,
            "base_color": (119, 110, 101),
            "hover_color": (150, 140, 130),
            "text_color": (255, 255, 255)
        }

        quit_button_data = {"rect": quit_button,
            "text": "Quit",
            "font": button_font,
            "screen": screen,
            "mouse": mouse_pos,
            "click": click,
            "base_color": (119, 110, 101),
            "hover_color": (150, 140, 130),
            "text_color": (255, 255, 255)
        }

        if button(start_button_data):
            main()
            return

        if button(quit_button_data):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

def lose_screen():
    config = GameConfig
    screen = pygame.display.get_surface()

    lose_font = pygame.font.SysFont("arial", 70)
    button_font = pygame.font.SysFont("arial", 30)

    restart_button = pygame.Rect(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 50, 200, 50)
    quit_button = pygame.Rect(config.WIDTH // 2 - 100, config.HEIGHT // 2 - 30, 200, 50)
    clock = pygame.time.Clock()

    board_snapshot = screen.copy()

    fade_overlay = pygame.Surface((config.WIDTH, config.HEIGHT))
    fade_overlay.fill((0, 0, 0))
    fade_overlay.set_alpha(150)

    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(board_snapshot, (0, 0))
        screen.blit(fade_overlay, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        pos = (config.WIDTH // 2, config.HEIGHT // 3)
        draw_text("Game Over", lose_font, (255, 255, 255), screen, pos)

        restart_button_data = {"rect": restart_button,
            "text": "Restart",
            "font": button_font,
            "screen": screen,
            "mouse": mouse_pos,
            "click": click,
            "base_color": (119, 110, 101),
            "hover_color": (150, 140, 130),
            "text_color": (255, 255, 255)
        }

        quit_button_data = {"rect": quit_button,
            "text": "Quit",
            "font": button_font,
            "screen": screen,
            "mouse": mouse_pos,
            "click": click,
            "base_color": (119, 110, 101),
            "hover_color": (150, 140, 130),
            "text_color": (255, 255, 255)
        }

        if button(restart_button_data):
            main()
        if button(quit_button_data):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.font.init()
    config = GameConfig()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    board = GameLogic()
    ui = BoardUI(board, screen, config)
    clock = pygame.time.Clock()

    running = True
    while running:
        if board.game_over:
            ui.check_top_score()
            lose_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    board.move("left")
                if event.key == pygame.K_RIGHT:
                    board.move("right")
                if event.key == pygame.K_UP:
                    board.move("up")
                if event.key == pygame.K_DOWN:
                    board.move("down")

        screen.fill(config.BG_COLOR)
        ui.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    start_menu()
