import random

class GameLogic:
    def __init__(self):
        # Initialize the game grid
        self.grid = [[0]*4 for _ in range(4)]
        self.score = 0

        # Game starts with two random tiles
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        # Adds a 2 or 4 to a empty cell
        empty_cells = []
        for row in range(4):
            for col in range(4):
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


    def move(self, input):
        method_name = "_move_" + input
        method = getattr(self, method_name)
        method()
        self.spawn_tile()

    def _move_left(self):
        pass

    def merge_row(self, row):
        # Merge tiles in a row
        new_row = [0]*4
        index = 0
        for cell in row:
            if cell == 0:
                continue
            if new_row[index] == 0:
                new_row[index] = cell
            elif new_row[index] == cell:
                new_row[index] *= 2
                self.score += new_row[index]
                index += 1
            else:
                index += 1
                new_row[index] = cell
        return new_row

    def game_over(self):
        # Game over logic
        pass
