# pylint: disable=no-member
# Pylint does not recognize pygame for some reason

import sys

import pygame

from game.game_logic import GameLogic
from game.top_score import TopScore
from game_config import GameConfig
from ui.board_ui import BoardUI

def draw_text(text, font, color, surface, pos):
    """
    Render given text at the given position

    Args:
        text: The string to render
        font: What font the text will be rendered in
        color: What color the text will be (RGB)
        surface: Target surface to draw the text on
        pos: The x and y cordinates of the text
    """
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(pos[0],pos[1]))
    surface.blit(textobj, textrect)

def button(data):
    """
    Draw a button with given data, detect hover and click

    Args:
        data(dict): Dictionary with all data for the button:
            rect: Button dimentions and position
            font: What font the text will be rendered in
            screen: The surface to draw on
            mouse: Current mouse coordinates (x, y)
            click: Weather the mouse has been clicked (bool)
            base_color: Default color of the button
            hover_color: Color for the button when hovered over
            text:color: Color for the text

    Return:
        bool: True if button is clicked, else False
            """
    color = data["hover_color"] if data["rect"].collidepoint(data["mouse"]) else data["base_color"]
    pygame.draw.rect(data["screen"], color, data["rect"], border_radius=10)
    pos = (data["rect"].centerx, data["rect"].centery)
    draw_text(data["text"], data["font"], data["text_color"],
       data["screen"], pos)
    return data["rect"].collidepoint(data["mouse"]) and data["click"]

def start_menu():
    """
    Display start menu, handels users input for starting game or quitting

    Checks if the top score folder and file exists, creates if needed.
    Initializes the Pygame.
    Creates "Start Game" and "Quit" buttons and causes their actions upon being pressed
    """
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
    """
    Dispalys the "Game Over" screen with the current game in the background faded out

    Shows "Game Over" text and buttons with "Restart" and "Quit". Handels the actions
    for these buttons
    """
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
    """
    Initializes and runs the loop of the game

    Setups the basics for the game
    Processes input events to move tiles or quit the game
    Triggers lose screen and runs until either lose screen or user quitting
    """
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
