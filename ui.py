import pygame
from settings import *

# ==========================================
# Gradient Background
# ==========================================
def draw_background(screen):

    for y in range(HEIGHT):

        color = (
            238 - y // 20,
            245 - y // 22,
            255
        )

        pygame.draw.line(
            screen,
            color,
            (0, y),
            (WIDTH, y)
        )


# ==========================================
# Game Title
# ==========================================
def draw_title(screen):

    title = TITLE_FONT.render(
        "🧩 Memory Puzzle Game PRO",
        True,
        DARK_BLUE
    )

    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, 55))
    )


# ==========================================
# HUD
# ==========================================
def draw_hud(screen, moves, score, seconds, pairs, high_score):

    move = HEADER_FONT.render(
        f"🎯 Moves : {moves}",
        True,
        BLACK
    )

    score_text = HEADER_FONT.render(
        f"⭐ Score : {score}",
        True,
        GREEN
    )

    timer = HEADER_FONT.render(
        f"⏰ Time : {seconds}",
        True,
        RED
    )

    pair = HEADER_FONT.render(
        f"🧩 Pairs : {pairs}/8",
        True,
        DARK_BLUE
    )

    high = HEADER_FONT.render(
        f"🏆 High : {high_score}",
        True,
        ORANGE
    )

    screen.blit(move, (25, 120))
    screen.blit(score_text, (250, 120))
    screen.blit(pair, (500, 120))
    screen.blit(timer, (760, 120))
    screen.blit(high, (965, 120))


# ==========================================
# Draw Cards
# ==========================================
def draw_cards(screen, cards):

    for card in cards:

        shadow = card["rect"].copy()

        shadow.x += 5
        shadow.y += 5

        pygame.draw.rect(
            screen,
            CARD_SHADOW,
            shadow,
            border_radius=18
        )

        if card["revealed"] or card["matched"]:

            pygame.draw.rect(
                screen,
                CARD_FRONT,
                card["rect"],
                border_radius=18
            )

            pygame.draw.rect(
                screen,
                CARD_BORDER,
                card["rect"],
                2,
                border_radius=18
            )

            value = CARD_FONT.render(
                str(card["value"]),
                True,
                CARD_TEXT
            )

            screen.blit(
                value,
                value.get_rect(
                    center=card["rect"].center
                )
            )

        else:

            pygame.draw.rect(
                screen,
                CARD_BACK,
                card["rect"],
                border_radius=18
            )

            pygame.draw.rect(
                screen,
                WHITE,
                card["rect"],
                2,
                border_radius=18
            )

            question = CARD_FONT.render(
                "?",
                True,
                WHITE
            )

            screen.blit(
                question,
                question.get_rect(
                    center=card["rect"].center
                )
            )


# ==========================================
# Professional Button
# ==========================================
def draw_button(screen, rect, text, color):

    mouse = pygame.mouse.get_pos()

    button_color = color

    if rect.collidepoint(mouse):

        button_color = YELLOW

    pygame.draw.rect(
        screen,
        button_color,
        rect,
        border_radius=BUTTON_RADIUS
    )

    pygame.draw.rect(
        screen,
        BLACK,
        rect,
        2,
        border_radius=BUTTON_RADIUS
    )

    label = BUTTON_FONT.render(
        text,
        True,
        BLACK
    )

    screen.blit(
        label,
        label.get_rect(center=rect.center)
    )


# ==========================================
# Win Popup
# ==========================================
def draw_win_popup(screen, score, moves):

    popup = pygame.Rect(
        250,
        220,
        700,
        320
    )

    pygame.draw.rect(
        screen,
        WHITE,
        popup,
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        GREEN,
        popup,
        4,
        border_radius=20
    )

    title = POPUP_FONT.render(
        "🏆 YOU WIN!",
        True,
        GREEN
    )

    screen.blit(
        title,
        title.get_rect(center=(600, 270))
    )

    info = [

        f"⭐ Score : {score}",
        f"🎯 Moves : {moves}",
        "",
        "Press R to Play Again",
        "Press ESC to Exit"

    ]

    y = 330

    for line in info:

        text = TEXT_FONT.render(
            line,
            True,
            BLACK
        )

        screen.blit(
            text,
            text.get_rect(center=(600, y))
        )

        y += 40


# ==========================================
# Game Over Popup
# ==========================================
def draw_gameover_popup(screen):

    popup = pygame.Rect(
        250,
        220,
        700,
        300
    )

    pygame.draw.rect(
        screen,
        WHITE,
        popup,
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        RED,
        popup,
        4,
        border_radius=20
    )

    title = POPUP_FONT.render(
        "⏰ TIME OVER!",
        True,
        RED
    )

    screen.blit(
        title,
        title.get_rect(center=(600, 280))
    )

    text = TEXT_FONT.render(
        "Press R to Restart",
        True,
        BLACK
    )

    screen.blit(
        text,
        text.get_rect(center=(600, 370))
    )


# ==========================================
# Footer
# ==========================================
def draw_footer(screen):

    footer = SMALL_FONT.render(
        "Developed with Python & Pygame",
        True,
        BLACK
    )

    screen.blit(
        footer,
        (20, HEIGHT - 28)
    )