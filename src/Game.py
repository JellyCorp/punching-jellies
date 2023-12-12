import pygame
import sys
import os

from frontend.MainMenu import MainMenu


class Game:
    def __init__(self):
        # SETTINGS
        self.fps = 60
        self.possible_start_positions = [
            [(368, 20)],
            [(368, 20), (368, 20)],
            [(368, 20), (368, 334), (368, 648)],
            [(368, 20), (368, 20), (368, 20), (368, 20)],
        ]

        # PYGAME
        pygame.init()
        pygame.display.set_caption("Punching Jellies")
        self.clock = pygame.time.Clock()

        # SETUP SCREEN
        SCREEN = {"width": 700, "height": 500}
        self.grid_dim = (SCREEN["height"], SCREEN["width"])
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        try:
            assert screen_width >= SCREEN["width"] and screen_height >= SCREEN["height"]
        except:
            raise Exception(
                f"Your screen dimensions ({screen_width}x{screen_height}) are too small ({SCREEN['width']}x{SCREEN['height']} is required)"
            )
        os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (
            (screen_width - SCREEN["width"]) // 2,
            (screen_height - SCREEN["height"]) // 2 - 40,
        )

        # RUN SCREEN
        self.screen = pygame.display.set_mode((SCREEN["width"], SCREEN["height"]))

        # MENU
        self.window = MainMenu(self)

        # LOOP
        while True:
            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    self.window.handle_event(event)

            # UPDATE
            cursor = self.window.update(pygame.mouse.get_pos())
            pygame.mouse.set_cursor(cursor)

            # DISPLAY
            pygame.display.flip()

            # FPS LOCK
            self.clock.tick(self.fps)


if __name__ == "__main__":
    # WORKING DIR
    WORKING_DIRECTORY = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(WORKING_DIRECTORY)
    Game()
