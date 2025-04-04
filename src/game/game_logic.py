import random
from game_config import GameConfig


class GameLogic:
    def __init__(self):
        # Initialize the game grid
        self.grid = [[0]*4 for _ in range(GameConfig.TILE_COUNT)]
        self.score = 0
        self.tile_count = GameConfig.TILE_COUNT

        # Game starts with two random tiles
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        # Adds a 2 or 4 to a empty cell
        empty_cells = []
        for row in range(0, self.tile_count):
            for col in range(0, self.tile_count):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))

        if empty_cells:
            row, col = random.choice(empty_cells)
            # 2 has a 90% chance of being spawned, 4 has a 10% chance
            if random.random() < 0.1:
                self.grid[row][col] = 4
            else:
                self.grid[row][col] = 2
        else:
            self.game_over()

    def move(self, input_key):
        method_name = "_move_" + input_key
        method = getattr(self, method_name)
        if method():
            self.spawn_tile()
        print(self.score)

    def _move_left(self):
        new_grid = []

        for original_row in self.grid:
            row = [i for i in original_row if i != 0]

            i = 0
            while i < len(row) - 1:
                if row[i] == row[i + 1]:
                    row[i] = row[i] * 2
                    self.score += row[i]
                    row.pop(i + 1)
                    row.append(0)
                i += 1

            row = [i for i in row if i != 0]
            row += [0] * (GameConfig.TILE_COUNT - len(row))

            new_grid.append(row)

        if new_grid == self.grid:
            return False
        self.grid = new_grid
        return True

    def _move_right(self):
        new_grid = []

        for original_row in self.grid:
            row = [i for i in original_row if i != 0]

            i = len(row) - 1
            while i > 0:
                if row[i] == row[i - 1]:
                    row[i] = row[i] * 2
                    self.score += row[i]
                    row.pop(i - 1)
                    row.insert(0, 0)
                i -= 1

            row = [i for i in row if i != 0]
            row = [0] * (GameConfig.TILE_COUNT - len(row)) + row

            new_grid.append(row)

        if new_grid == self.grid:
            return False
        self.grid = new_grid
        return True

    def _move_up(self):
        new_grid = [
            [0] * GameConfig.TILE_COUNT for _ in range(GameConfig.TILE_COUNT)]

        for col in range(GameConfig.TILE_COUNT):
            col_vals = [self.grid[row][col]
                        for row in range(GameConfig.TILE_COUNT)]
            col_vals = [val for val in col_vals if val != 0]

            i = 0
            while i < len(col_vals) - 1:
                if col_vals[i] == col_vals[i + 1]:
                    col_vals[i] *= 2
                    self.score += col_vals[i]
                    col_vals.pop(i + 1)
                    col_vals.append(0)
                i += 1

            col_vals = [val for val in col_vals if val != 0]
            new_col = col_vals + [0] * (GameConfig.TILE_COUNT - len(col_vals))

            for row in range(GameConfig.TILE_COUNT):
                new_grid[row][col] = new_col[row]

        if new_grid == self.grid:
            return False
        self.grid = new_grid
        return True

    def _move_down(self):
        new_grid = [
            [0] * GameConfig.TILE_COUNT for _ in range(GameConfig.TILE_COUNT)]

        for col in range(GameConfig.TILE_COUNT):
            col_vals = [self.grid[row][col]
                        for row in range(GameConfig.TILE_COUNT)]
            col_vals = [val for val in col_vals if val != 0]

            i = len(col_vals) - 1
            while i > 0:
                if col_vals[i] == col_vals[i - 1]:
                    col_vals[i] *= 2
                    self.score += col_vals[i]
                    col_vals.pop(i - 1)
                    col_vals.insert(0, 0)
                i -= 1

            col_vals = [val for val in col_vals if val != 0]
            new_col = [0] * (GameConfig.TILE_COUNT - len(col_vals)) + col_vals

            for row in range(GameConfig.TILE_COUNT):
                new_grid[row][col] = new_col[row]

        if new_grid == self.grid:
            return False
        self.grid = new_grid
        return True

    def game_over(self):
        # Game over logic
        pass
