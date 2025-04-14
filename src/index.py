# pylint: disable=no-member
# Pylint does not recognize pygame for some reason
import sys
import pygame
from game.game_logic import GameLogic
from ui.board_ui import BoardUI
from game_config import GameConfig

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x,y))
    surface.blit(textobj, textrect)

def button(rect, text, font, screen, mouse_pos, click, base_color, hover_color, text_color):
    color = hover_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(screen, color, rect, border_radius=10)
    draw_text(text, font, text_color, screen, rect.centerx, rect.centery)
    return rect.collidepoint(mouse_pos) and click

def start_menu():
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mouse_pos = pygame.mouse.get_pos()
        screen.fill(config.BG_COLOR)

        draw_text("2048", title_font, (119,110,101), screen, config.WIDTH // 2, config.HEIGHT // 3)

        if button(start_button, "Start Game", button_font, screen, mouse_pos, click,
            (119, 110, 101), (150, 140, 130), (255, 255, 255)):
            main()
            return

        if button(quit_button, "Quit", button_font, screen, mouse_pos, click,
            (119, 110, 101), (150, 140, 130), (255, 255, 255)):
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

        draw_text("Game Over", lose_font, (255, 255, 255), screen,
            config.WIDTH // 2, config.HEIGHT // 3)

        if button(restart_button, "Restart", button_font, screen, mouse_pos, click,
            (119, 110, 101), (150, 140, 130), (255, 255, 255)):
            return "restart"
        if button(quit_button, "Quit", button_font, screen, mouse_pos, click,
            (119, 110, 101), (150, 140, 130), (255, 255, 255)):
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
