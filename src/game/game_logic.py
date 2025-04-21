import random
import pygame
from game_config import GameConfig

class Tile:
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
    def __init__(self):
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
        # Generated with help from AI
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
