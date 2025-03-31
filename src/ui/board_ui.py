from game.game_logic import GameLogic
import pygame
from game_config import GameConfig

class BoardUI:
    def __init__(self, board, screen, config):
        self.board = board
        self.screen = screen
        self.config = config
        self.tile_size = config.TILE_SIZE
        self.spacing = config.SPACING

    def draw(self):
        font = pygame.font.Font(None, 48)

        for i in range(GameConfig.TILE_COUNT):
            for j in range(GameConfig.TILE_COUNT):
                value = self.board.grid[i][j]
                color = self.config.TILE_COLORS.get(value)

                rect = pygame.Rect(
                    j*(self.tile_size + self.spacing) + self.spacing,
                    i*(self.tile_size + self.spacing) + self.spacing,
                    self.tile_size,
                    self.tile_size
                )
                pygame.draw.rect(self.screen, color, rect)

                if value != 0:
                    text_surface = font.render(str(value), True, (0, 0, 0))  # Render text in black
                    text_rect = text_surface.get_rect(center=rect.center)  # Center text in the tile
                    self.screen.blit(text_surface, text_rect)  # Draw the text
