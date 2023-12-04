import pygame

from windows.Window import Window
from sprites.Button import Button
from sprites.Text import Text


class Battlefield(Window):
    def __init__(self, game):
        super().__init__(game)

        # TEXTS

        # BUTTONS

        # ADDING SPRITES TO INITIAL GROUPS
        self.buttons.add([])
        self.texts.add([])

        # MUSIC
        #pygame.mixer.music.set_volume(0.05)
        #pygame.mixer.music.load("../assets/audio/music/main_theme.mp3")
        #pygame.mixer.music.play(-1)

    def next_window(self):
        pass

    def previous_window(self):
        pass