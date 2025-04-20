import pygame
from game_config import GameConfig
from game.top_score import TopScore

class BoardUI:
    def __init__(self, board, screen, config):
        self.board = board
        self.screen = screen
        self.config = config
        self.tile_size = config.TILE_SIZE
        self.spacing = config.SPACING
        self.top_score = TopScore()
        self.current_top_score = self.top_score.load_top_score()

    def draw(self):
        font = pygame.font.SysFont("arial", 32)

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
                    text_surface = font.render(
                        str(value), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(
                        center=rect.center)
                    self.screen.blit(text_surface, text_rect)

        score_text = font.render("Score: " + str(self.board.score), True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.midbottom = (self.screen.get_width() // 2, self.screen.get_height() - 60)
        self.screen.blit(score_text, score_rect)

        top_score_text = font.render("Top Score: " + str(self.current_top_score), True, (255, 255, 255))
        top_score_rect = top_score_text.get_rect()
        top_score_rect.midbottom = (self.screen.get_width() // 2, self.screen.get_height() - 10)
        self.screen.blit(top_score_text, top_score_rect)

    def check_top_score(self):
        if self.board.score > self.current_top_score:
            self.current_top_score = self.board.score
            self.top_score.save_top_score(self.current_top_score)
        return 0
