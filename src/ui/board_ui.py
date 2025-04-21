import pygame
from game_config import GameConfig
from game.top_score import TopScore

class BoardUI:
    """
    Shows the visual representation of the game loop

    Draws the game board, tiles, animations, current score and top score
    """
    def __init__(self, board, screen, config):
        """
        Initializes the BoardUI class

        Args:
            board: The game board object
            screen: The game screen object
            config: The game configuration object
            tile_size: The dimentions for the tiles
            spacing: The amount of space between tiles
            top_score = The top score class
            current_top_score: Gets the current top score from the top_score
            animation_time: The duration of the animation
        """
        self.board = board
        self.screen = screen
        self.config = config
        self.tile_size = config.TILE_SIZE
        self.spacing = config.SPACING

        self.top_score = TopScore()
        self.current_top_score = self.top_score.load_top_score()

        self.animation_time = config.ANIMATION_DURATION

    def draw(self):
        """
        Function responsible for drawing everyting

        Actions:
            Drawing the background
            Drawing the tiles
            Drawing the animations for tiles
            Drawing the score
            Drawing the top score
            Drawing the game over message when needed
        """
        self.screen.fill(self.config.BG_COLOR)
        font = pygame.font.SysFont("arial", 32)
        now = pygame.time.get_ticks()

        for r in range(GameConfig.TILE_COUNT):
            for c in range(GameConfig.TILE_COUNT):

                x = c * (self.tile_size + self.spacing) + self.spacing
                y = r * (self.tile_size + self.spacing) + self.spacing
                base_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)

                pygame.draw.rect(
                    self.screen,
                    self.config.EMPTY_TILE_COLOR,
                    base_rect,
                    border_radius=4
                )

                tile = self.board.grid[r][c]
                if tile is None:
                    continue

                # Code for animation, written with help of AI
                dt_move = now - tile.move_start
                t_move = min(1, dt_move / self.animation_time)
                row_pos = tile.previous_row + (tile.row - tile.previous_row) * t_move
                col_pos = tile.previous_col + (tile.col - tile.previous_col) * t_move

                px = col_pos * (self.tile_size + self.spacing) + self.spacing
                py = row_pos * (self.tile_size + self.spacing) + self.spacing
                rect = pygame.Rect(px, py, self.tile_size, self.tile_size)

                dt_spawn = now - tile.spawn_time
                if dt_spawn < self.animation_time:
                    t_spawn = dt_spawn / self.animation_time
                    shrink = int(self.tile_size * (1 - t_spawn) / 2)
                    rect.inflate_ip(-shrink*2, -shrink*2)
                # End of code part for animation

                color = self.config.TILE_COLORS[tile.value]
                pygame.draw.rect(
                    self.screen,
                    color,
                    rect,
                    border_radius=4
                )

                text_surf = font.render(str(tile.value), True, self.config.TEXT_COLOR)
                text_rect = text_surf.get_rect(center=rect.center)
                self.screen.blit(text_surf, text_rect)

        score_txt = font.render(f"Score: {self.board.score}", True, (255, 255, 255))
        score_rect = score_txt.get_rect(midbottom=(
            self.screen.get_width() // 2,
            self.screen.get_height() - 60
        ))
        self.screen.blit(score_txt, score_rect)

        top_txt = font.render(f"Top Score: {self.current_top_score}", True, (255, 255, 255))
        top_rect = top_txt.get_rect(midbottom=(
            self.screen.get_width() // 2,
            self.screen.get_height() - 10
        ))
        self.screen.blit(top_txt, top_rect)


    def check_top_score(self):
        """
        Checks if the currently gotten score at the end of the game
        is larger than the top score, and updates the top score if necessary
        """
        if self.board.score > self.current_top_score:
            self.current_top_score = self.board.score
            self.top_score.save_top_score(self.current_top_score)
        return 0
