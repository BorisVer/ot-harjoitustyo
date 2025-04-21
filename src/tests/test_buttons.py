import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import index
import pygame

class TestButtons(unittest.TestCase):
    def setUp(self):
        # Make a mock game instance
        pygame.init()
        pygame.font.init()
        self.screen = pygame.Surface((800, 600))
        self.font = pygame.font.SysFont("arial", 24)
        self.button_data = {
            "rect": pygame.Rect(50, 50, 100, 40),
            "text": "Test",
            "font": self.font,
            "screen": self.screen,
            "mouse": (0, 0),
            "click": False,
            "base_color": (100, 100, 100),
            "hover_color": (150, 150, 150),
            "text_color": (255, 255, 255)
        }

    def test_clicking_button_works(self):
        data = self.button_data.copy()
        data["mouse"] = (75, 75)
        data["click"] = True
        result = index.button(data)
        self.assertTrue(result)

    def test_clicking_outside_button_does_not_activate(self):
        data = self.button_data.copy()
        data["mouse"] = (0, 0)
        data["click"] = True
        result = index.button(data)
        self.assertFalse(result)

    def test_hovering_does_not_activate(self):
        data = self.button_data.copy()
        data["mouse"] = (75, 75)
        data["click"] = False
        result = index.button(data)
        self.assertFalse(result)
