import pygame
from game.game_logic import GameLogic
from ui.board_ui import BoardUI
from game_config import GameConfig

def main():
    pygame.init()
    config = GameConfig()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    board = GameLogic()
    ui = BoardUI(board, screen, config)
    clock = pygame.time.Clock()

    running = True
    while running:
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
    main()
