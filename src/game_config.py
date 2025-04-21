class GameConfig:
    """
    All data that can be modified as needed to change the game

    Args:
        TILE_COUNT: How many tiles in each row and how many columns
        WIDTH: Width of the screen
        HEIGHT: Height of the screen
        TILE_SIZE: The size of the tiles
        SPACING: The space between tiles
        BG_COLOR: The background color for the game
        EMPTY_TILE_COLOR: Color for spaces that are not occupied by tiles
        TEXT_COLOR: Standard color for text in the game
        TILE_COLORS: All colors for tiles at each value
        ANIMATION_DURATION: Duration of animations in milliseconds
    """
    TILE_COUNT = 4
    WIDTH = 400
    HEIGHT = 500
    TILE_SIZE = 80
    SPACING = 15
    BG_COLOR = (187, 173, 160)
    EMPTY_TILE_COLOR = (205, 193, 180)
    TEXT_COLOR       = (0,   0,   0)
    TILE_COLORS = {
        # Generoitu koodi alkaa (deepseek)
        0: (205, 193, 180),
        2: (255, 223, 186),
        4: (255, 190, 122),
        8: (255, 127, 80),
        16: (255, 99, 71),
        32: (255, 40, 30),
        64: (220, 20, 60),
        128: (186, 85, 211),
        256: (147, 112, 219),
        512: (100, 149, 237),
        1024: (72, 209, 204),
        2048: (60, 179, 113),
        4096: (255, 215, 0),
        8192: (255, 140, 0),
        16384: (255, 69, 0),
        32768: (139, 0, 139),
        65536: (75, 0, 130),
        # Generoitu koodi loppuu
    }
    ANIMATION_DURATION = 100
