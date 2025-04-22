import random
import pygame
from game_config import GameConfig

class Tile:
    """
    Represents a tile in the game grid.

    Attributes:
        value: The value of the tile (2,4,8,...)
        row: The row index of the tile
        col: The column index of the tile
        previous_row: The previous row index of the tile (needed purely for animation)
        previous_col: The previous column index of the tile (needed purely for animation)
        spawn_time: The time when the tile was spawned (needed purely for animation)
        move_start: The time when the tile started moving (needed purely for animation)
    """
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.previous_row = row
        self.previous_col = col
        now = pygame.time.get_ticks()
        self.spawn_time = now
        self.move_start = now

# --------------------------------------
class GameLogic:
    """
    Manages game rules and states:
        Tile spawning
        Tile sliding
        Tile merging
        Score calculation
        Game over detection
    """

    def __init__(self):
        """
        Initializes the game state

        Attributes:
            tile_count: The number of tiles in the grid (from GameConfig file, standard 4)
            score: The current score of the game
            game_over: Indicates if the game is over
            grid: The 2D grid representing the game board
            last_spawned_tile: The position of the last spawned tile
            spawn_time: The time when the last tile was spawned
        """
        self.tile_count = GameConfig.TILE_COUNT
        self.score = 0
        self.game_over = False

        self.grid = [[None] * self.tile_count for _ in range(self.tile_count)]
        self.last_spawned_tile = None
        self.spawn_time = 0

        # start with two tiles
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        """
        Spawns a new tile at a random empty position

        Tile has a 90% probablity of being 2, 10% of being 4

        Returns:
            Tile: The newly spawned tile, or None if no empty positions are available
        """
        empty = [
            (r, c)
            for r in range(self.tile_count)
            for c in range(self.tile_count)
            if self.grid[r][c] is None
        ]
        if not empty:
            return None

        row, col = random.choice(empty)
        value = 4 if random.random() < 0.1 else 2
        tile = Tile(value, row, col)
        self.grid[row][col] = tile

        self.last_spawned_tile = (row, col)
        self.spawn_time = tile.spawn_time
        return tile

    def move(self, input_key):
        """
        Executes a move based on the input given

        Records tile movement history, calles the appropriate move and spawns a new tile
        Calls the is_game_over to check if game is over after each move, ends game if True

        Args:
            input_key: A string representing the direction
            of the move ('up', 'down', 'left', 'right')
        """
        now = pygame.time.get_ticks()
        for r in range(self.tile_count):
            for tile in self.grid[r]:
                if tile:
                    tile.previous_row = tile.row
                    tile.previous_col = tile.col
                    tile.move_start = now

        self.last_spawned_tile = None

        method = getattr(self, f"_move_{input_key}")
        if method():
            self.spawn_tile()
        if self._is_game_over():
            self.game_over = True

    def _move_left(self):
        """
        Slides all tiles to the left. Merges equal tiles

        Returns:
            bool: True if any tile moved, False otherwise
        """
        moved = False
        for r in range(self.tile_count):
            tiles = [t for t in self.grid[r] if t]
            c = 0
            while c < len(tiles) - 1:
                if tiles[c].value == tiles[c+1].value:
                    tiles[c].value *= 2
                    self.score += tiles[c].value
                    del tiles[c+1]
                c += 1
            for idx, t in enumerate(tiles):
                t.row, t.col = r, idx
            new_row = tiles + [None] * (self.tile_count - len(tiles))
            if new_row != self.grid[r]:
                moved = True
                self.grid[r] = new_row
        return moved

    def _move_right(self):
        """
        Slides all tiles to the right. Merges equal tiles

        Returns:
            bool: True if any tile moved, False otherwise
        """
        moved = False
        for r in range(self.tile_count):
            tiles = [t for t in self.grid[r] if t]
            c = len(tiles) - 1
            while c > 0:
                if tiles[c].value == tiles[c-1].value:
                    tiles[c].value *= 2
                    self.score += tiles[c].value
                    del tiles[c-1]
                    c -= 1
                c -= 1
            for idx, t in enumerate(reversed(tiles)):
                t.row, t.col = r, self.tile_count - 1 - idx
            new_row = [None] * (self.tile_count - len(tiles)) + tiles
            if new_row != self.grid[r]:
                moved = True
                self.grid[r] = new_row
        return moved

    def _move_up(self):
        """
        Slides all tiles up. Merges equal tiles

        Returns:
            bool: True if any tile moved, False otherwise
        """
        moved = False
        for c in range(self.tile_count):
            col_tiles = [self.grid[r][c] for r in range(self.tile_count) if self.grid[r][c]]
            i = 0
            while i < len(col_tiles) - 1:
                if col_tiles[i].value == col_tiles[i+1].value:
                    col_tiles[i].value *= 2
                    self.score += col_tiles[i].value
                    del col_tiles[i+1]
                i += 1
            for idx, t in enumerate(col_tiles):
                t.row, t.col = idx, c
            new_col = col_tiles + [None] * (self.tile_count - len(col_tiles))
            for r in range(self.tile_count):
                if self.grid[r][c] != new_col[r]:
                    moved = True
                    self.grid[r][c] = new_col[r]
        return moved

    def _move_down(self):
        """
        Slides all tiles down. Merges equal tiles

        Returns:
            bool: True if any tile moved, False otherwise
        """
        moved = False
        for c in range(self.tile_count):
            col_tiles = [self.grid[r][c] for r in range(self.tile_count) if self.grid[r][c]]
            i = len(col_tiles) - 1
            while i > 0:
                if col_tiles[i].value == col_tiles[i-1].value:
                    col_tiles[i].value *= 2
                    self.score += col_tiles[i].value
                    del col_tiles[i-1]
                    i -= 1
                i -= 1
            for idx, t in enumerate(reversed(col_tiles)):
                t.row, t.col = self.tile_count - 1 - idx, c
            new_col = [None] * (self.tile_count - len(col_tiles)) + col_tiles
            for r in range(self.tile_count):
                if self.grid[r][c] != new_col[r]:
                    moved = True
                    self.grid[r][c] = new_col[r]
        return moved

    def _is_game_over(self):
        """
        Checks if there is any valid moves or empty tiles

        Returns:
            bool: True if game is over, False otherwise
        """
        # Generated with help of AI
        for r in range(self.tile_count):
            for c in range(self.tile_count):
                if self.grid[r][c] is None:
                    return False
                for dr, dc in ((1,0),(0,1)):
                    nr, nc = r+dr, c+dc
                    if nr < self.tile_count and nc < self.tile_count:
                        t1 = self.grid[r][c]
                        t2 = self.grid[nr][nc]
                        if t2 and t1.value == t2.value:
                            return False
        return True
