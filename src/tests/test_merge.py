import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game.game_logic import GameLogic

class TestMergeLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_merge_logic_left(self):
        self.game.grid = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("left")

        self.assertEqual(self.game.grid[1][0], 4)

    def test_merge_logic_right(self):
        self.game.grid = [
            [0, 0, 0, 0],
            [0, 0, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("right")

        self.assertEqual(self.game.grid[1][3], 4)

    def test_merge_logic_up(self):
        self.game.grid = [
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("up")

        self.assertEqual(self.game.grid[0][1], 4)

    def test_merge_logic_down(self):
        self.game.grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 2, 0]
        ]

        self.game.move("down")

        self.assertEqual(self.game.grid[3][2], 4)

    def test_double_merge(self):
        self.game.grid = [
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("right")

        self.assertEqual(self.game.grid[0][2:4], [4, 4])
