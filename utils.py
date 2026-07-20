import random
import pygame

from settings import *

# ==========================================
# Create Cards
# ==========================================
def create_cards():

    values = list(range(1, 9))
    values *= 2

    random.shuffle(values)

    cards = []

    index = 0

    for row in range(ROWS):

        for col in range(COLS):

            x = START_X + col * (CARD_SIZE + CARD_GAP)
            y = START_Y + row * (CARD_SIZE + CARD_GAP)

            rect = pygame.Rect(
                x,
                y,
                CARD_SIZE,
                CARD_SIZE
            )

            cards.append({

                "rect": rect,

                "value": values[index],

                "revealed": False,

                "matched": False

            })

            index += 1

    return cards


# ==========================================
# Restart Cards
# ==========================================
def restart_cards(cards):

    values = list(range(1, 9))
    values *= 2

    random.shuffle(values)

    for i, card in enumerate(cards):

        card["value"] = values[i]
        card["revealed"] = False
        card["matched"] = False


# ==========================================
# Find Clicked Card
# ==========================================
def clicked_card(cards, mouse_pos):

    for card in cards:

        if card["rect"].collidepoint(mouse_pos):

            return card

    return None


# ==========================================
# Match Check
# ==========================================
def cards_match(card1, card2):

    return card1["value"] == card2["value"]


# ==========================================
# Count Matched Pairs
# ==========================================
def matched_pairs(cards):

    matched = 0

    for card in cards:

        if card["matched"]:

            matched += 1

    return matched // 2


# ==========================================
# Game Finished
# ==========================================
def game_finished(cards):

    for card in cards:

        if not card["matched"]:

            return False

    return True


# ==========================================
# Score System
# ==========================================
def update_score(score, matched):

    if matched:

        score += 10

    else:

        score -= 2

        if score < 0:

            score = 0

    return score


# ==========================================
# Difficulty Time
# ==========================================
def difficulty_time(level):

    if level == "Easy":

        return 90

    elif level == "Hard":

        return 45

    return 60


# ==========================================
# High Score
# ==========================================
def load_high_score():

    try:

        with open(
            HIGH_SCORE_FILE,
            "r"
        ) as file:

            return int(file.read())

    except:

        return 0


def save_high_score(score):

    with open(
        HIGH_SCORE_FILE,
        "w"
    ) as file:

        file.write(str(score))


# ==========================================
# Timer
# ==========================================
def format_time(seconds):

    minutes = seconds // 60

    sec = seconds % 60

    return f"{minutes:02}:{sec:02}"


# ==========================================
# Random Card Color
# ==========================================
def random_color():

    colors = [

        BLUE,
        GREEN,
        ORANGE,
        PURPLE,
        YELLOW

    ]

    return random.choice(colors)


# ==========================================
# Draw Rounded Shadow
# ==========================================
def draw_shadow(screen, rect):

    shadow = rect.copy()

    shadow.x += 4
    shadow.y += 4

    pygame.draw.rect(

        screen,

        CARD_SHADOW,

        shadow,

        border_radius=18

    )


# ==========================================
# FPS Counter (Optional)
# ==========================================
def show_fps(screen, clock):

    if not SHOW_FPS:

        return

    fps = int(clock.get_fps())

    font = pygame.font.SysFont(
        "Arial",
        18
    )

    text = font.render(

        f"FPS : {fps}",

        True,

        RED

    )

    screen.blit(text, (10, 10))