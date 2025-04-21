import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.game_logic import GameLogic, Tile
from game_config import GameConfig
import unittest



class TestScoreLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.config = GameConfig()

    def _set_grid(self, start):
        for row in range(self.config.TILE_COUNT):
            for col in range(self.config.TILE_COUNT):
                value = start[row][col]
                self.game.grid[row][col] = Tile(value, row, col) if value else None


    def test_score_zero_at_start(self):
        self.assertEqual(self.game.score, 0)

    def test_single_merge_increase_score(self):
        start = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self._set_grid(start)
        self.game.move("left")

        self.assertEqual(self.game.score, 4)

    def test_multi_merge_increase_score(self):
        start = [
            [4, 4, 8, 8],
            [2, 2, 16, 16],
            [2, 2, 2, 2],
            [4, 4, 4, 4]
        ]
        self._set_grid(start)
        self.game.move("left")

        self.assertEqual(self.game.score, 84)

    def test_non_memrge_move_does_not_change_score(self):
        start = [
            [0, 0, 0, 0],
            [2, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self._set_grid(start)
        self.game.move("left")

        self.assertEqual(self.game.score, 0)
