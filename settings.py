import pygame

# ==========================================
# Initialize Fonts
# ==========================================
pygame.font.init()

# ==========================================
# Window
# ==========================================
WIDTH = 1200
HEIGHT = 800

TITLE = "🧩 Memory Puzzle Game PRO"

FPS = 60

# ==========================================
# Game Board
# ==========================================
ROWS = 4
COLS = 4

CARD_SIZE = 120
CARD_GAP = 20

BOARD_WIDTH = COLS * CARD_SIZE + (COLS - 1) * CARD_GAP
BOARD_HEIGHT = ROWS * CARD_SIZE + (ROWS - 1) * CARD_GAP

START_X = (WIDTH - BOARD_WIDTH) // 2
START_Y = 170

# ==========================================
# Game
# ==========================================
TIME_LIMIT = 60

FLIP_DELAY = 700

DEFAULT_DIFFICULTY = "Normal"

# ==========================================
# Colors
# ==========================================
BACKGROUND = (238, 245, 255)

WHITE = (255, 255, 255)

BLACK = (35, 35, 35)

BLUE = (52, 152, 219)

DARK_BLUE = (41, 128, 185)

GREEN = (46, 204, 113)

RED = (231, 76, 60)

YELLOW = (241, 196, 15)

GRAY = (210, 210, 210)

LIGHT_GRAY = (240, 240, 240)

ORANGE = (243, 156, 18)

PURPLE = (155, 89, 182)

# ==========================================
# Card Colors
# ==========================================
CARD_FRONT = GREEN

CARD_BACK = BLUE

CARD_BORDER = BLACK

CARD_TEXT = BLACK

CARD_SHADOW = (180, 180, 180)

# ==========================================
# Fonts
# ==========================================
TITLE_FONT = pygame.font.SysFont(
    "Arial",
    52,
    bold=True
)

HEADER_FONT = pygame.font.SysFont(
    "Arial",
    28,
    bold=True
)

CARD_FONT = pygame.font.SysFont(
    "Arial",
    48,
    bold=True
)

TEXT_FONT = pygame.font.SysFont(
    "Arial",
    24
)

BUTTON_FONT = pygame.font.SysFont(
    "Arial",
    30,
    bold=True
)

POPUP_FONT = pygame.font.SysFont(
    "Arial",
    38,
    bold=True
)

SMALL_FONT = pygame.font.SysFont(
    "Arial",
    20
)

# ==========================================
# Game States
# ==========================================
MENU = "menu"

PLAYING = "playing"

WIN = "win"

GAME_OVER = "game_over"

SETTINGS = "settings"

# ==========================================
# Assets
# ==========================================
BACKGROUND_IMAGE = None

CARD_BACK_IMAGE = None

LOGO_IMAGE = None

# ==========================================
# High Score
# ==========================================
HIGH_SCORE_FILE = "highscore.txt"

# ==========================================
# Sounds
# ==========================================
CLICK_SOUND = "assets/sounds/click.wav"

FLIP_SOUND = "assets/sounds/flip.wav"

MATCH_SOUND = "assets/sounds/match.wav"

WIN_SOUND = "assets/sounds/win.wav"

GAMEOVER_SOUND = "assets/sounds/gameover.wav"

BACKGROUND_MUSIC = "assets/sounds/music.mp3"

# ==========================================
# Button Sizes
# ==========================================
BUTTON_WIDTH = 240

BUTTON_HEIGHT = 60

BUTTON_RADIUS = 12

# ==========================================
# Animation
# ==========================================
ANIMATION_SPEED = 12

CONFETTI_COUNT = 120

SHOW_FPS = False