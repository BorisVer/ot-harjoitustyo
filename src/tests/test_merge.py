import sys
import os

from src.index import start_menu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.game_logic import GameLogic, Tile
from game_config import GameConfig
import unittest



class TestMergeLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.config = GameConfig()

    def _set_grid(self, start):
        for row in range(self.config.TILE_COUNT):
            for col in range(self.config.TILE_COUNT):
                value = start[row][col]
                self.game.grid[row][col] = Tile(value, row, col) if value else None


    def test_merge_logic_left(self):
        start = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self._set_grid(start)
        self.game.move("left")

        self.assertEqual(self.game.grid[1][0].value, 4)

    def test_merge_logic_right(self):
        start = [
            [0, 0, 0, 0],
            [0, 0, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self._set_grid(start)
        self.game.move("right")

        self.assertEqual(self.game.grid[1][3].value, 4)

    def test_merge_logic_up(self):
        start = [
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self._set_grid(start)
        self.game.move("up")


        self.assertEqual(self.game.grid[0][1].value, 4)

    def test_merge_logic_down(self):
        start = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 2, 0]
        ]

        self._set_grid(start)
        self.game.move("down")

        self.assertEqual(self.game.grid[3][2].value, 4)

    def test_double_merge(self):
        start = [
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self._set_grid(start)
        self.game.move("right")

        self.assertEqual([self.game.grid[0][2].value,
            self.game.grid[0][3].value], [4, 4])
