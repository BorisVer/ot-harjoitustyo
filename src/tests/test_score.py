import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.game_logic import GameLogic
import unittest



class TestScoreLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_score_zero_at_start(self):
        self.assertEqual(self.game.score, 0)

    def test_single_merge_increase_score(self):
        self.game.grid = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("left")

        self.assertEqual(self.game.score, 4)

    def test_multi_merge_increase_score(self):
        self.game.grid = [
            [4, 4, 8, 8],
            [2, 2, 16, 16],
            [2, 2, 2, 2],
            [4, 4, 4, 4]
        ]

        self.game.move("left")

        self.assertEqual(self.game.score, 84)

    def test_non_memrge_move_does_not_change_score(self):
        self.game.grid = [
            [0, 0, 0, 0],
            [2, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.game.move("left")

        self.assertEqual(self.game.score, 0)
