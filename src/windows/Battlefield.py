import pygame

from windows.Window import Window
from sprites.Button import Button
from sprites.Text import Text


class Battlefield(Window):
    def __init__(self, game):
        super().__init__(game)
        self.background_color = (255, 255, 255)

        # TEXTS

        # BUTTONS
        self.ground = Button(
            (0, 400), None, None, background_color=(0, 0, 0), rect_size=(700, 10)
        )

        # ADDING SPRITES TO INITIAL GROUPS
        self.buttons.add([self.ground])
        self.texts.add([])

        # MUSIC
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.load("../assets/audio/music/battle_theme.mp3")
        pygame.mixer.music.play(-1)

    def next_window(self):
        pass

    def previous_window(self):
        pass
