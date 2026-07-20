import pygame
import sys

from settings import *
from ui import *
from utils import *


class MemoryPuzzleGame:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        # Game Data
        self.cards = create_cards()

        self.first_card = None
        self.second_card = None

        self.moves = 0
        self.score = 0

        self.waiting = False
        self.wait_start = 0

        self.running = True

        self.state = PLAYING

        self.high_score = load_high_score()

        self.start_ticks = pygame.time.get_ticks()

        self.time_limit = difficulty_time(
            DEFAULT_DIFFICULTY
        )

    # =====================================
    # Remaining Time
    # =====================================
    def remaining_time(self):

        elapsed = (
            pygame.time.get_ticks()
            - self.start_ticks
        ) // 1000

        remain = self.time_limit - elapsed

        return max(0, remain)

    # =====================================
    # Time Over
    # =====================================
    def time_over(self):

        return self.remaining_time() <= 0

    # =====================================
    # Player Win
    # =====================================
    def player_won(self):

        return game_finished(self.cards)

    # =====================================
    # Restart
    # =====================================
    def restart(self):

        restart_cards(self.cards)

        self.moves = 0
        self.score = 0

        self.first_card = None
        self.second_card = None

        self.waiting = False

        self.start_ticks = pygame.time.get_ticks()

        self.state = PLAYING

    # =====================================
    # High Score
    # =====================================
    def update_high_score(self):

        if self.score > self.high_score:

            self.high_score = self.score

            save_high_score(self.score)
                # =====================================
    # Handle Mouse Click
    # =====================================
    def handle_mouse_click(self, mouse_pos):

        if self.waiting:
            return

        if self.time_over():
            return

        if self.player_won():
            return

        card = clicked_card(self.cards, mouse_pos)

        if card is None:
            return

        if card["revealed"] or card["matched"]:
            return

        card["revealed"] = True

        # First Card
        if self.first_card is None:

            self.first_card = card
            return

        # Same Card
        if card == self.first_card:
            return

        # Second Card
        self.second_card = card

        self.moves += 1

        self.waiting = True

        self.wait_start = pygame.time.get_ticks()

    # =====================================
    # Check Match
    # =====================================
    def check_match(self):

        if self.first_card is None:
            return

        if self.second_card is None:
            return

        if cards_match(
            self.first_card,
            self.second_card
        ):

            self.first_card["matched"] = True
            self.second_card["matched"] = True

            self.score = update_score(
                self.score,
                True
            )

            self.update_high_score()

        else:

            self.first_card["revealed"] = False
            self.second_card["revealed"] = False

            self.score = update_score(
                self.score,
                False
            )

        self.first_card = None
        self.second_card = None

        self.waiting = False

    # =====================================
    # Update
    # =====================================
    def update(self):

        if self.waiting:

            current = pygame.time.get_ticks()

            if current - self.wait_start >= FLIP_DELAY:

                self.check_match()

        if self.player_won():

            self.state = WIN

        elif self.time_over():

            self.state = GAME_OVER

    # =====================================
    # Draw
    # =====================================
    def draw(self):

        draw_background(self.screen)

        draw_title(self.screen)

        draw_hud(

            self.screen,

            self.moves,

            self.score,

            self.remaining_time(),

            matched_pairs(self.cards),

            self.high_score

        )

        draw_cards(

            self.screen,

            self.cards

        )

        draw_footer(self.screen)

        if self.state == WIN:

            draw_win_popup(

                self.screen,

                self.score,

                self.moves

            )

        elif self.state == GAME_OVER:

            draw_gameover_popup(

                self.screen

            )

        show_fps(

            self.screen,

            self.clock

        )

        pygame.display.flip()

    # =====================================
    # Main Loop
    # =====================================
    def run(self):

        while self.running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.running = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        self.running = False

                    elif event.key == pygame.K_r:

                        self.restart()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    self.handle_mouse_click(

                        pygame.mouse.get_pos()

                    )

            self.update()

            self.draw()

        pygame.quit()

        sys.exit()


# =====================================
# Start Game
# =====================================
if __name__ == "__main__":

    game = MemoryPuzzleGame()

    game.run()