import pygame

from .jelly_ui.windows.Window import Window
from .jelly_ui.sprites.Button import Button
from .jelly_ui.sprites.Text import Text
from .jelly_ui.sprites.Entity import Entity


class Battlefield(Window):
    def __init__(self, game):
        super().__init__(game)
        self.background_color = (255,255,255)

        # TEXTS

        # BUTTONS
        self.ground = Button(
            (0, 400),
            None,
            None,
            background_color=(0,0,0),
            rect_size=(700,100)
        )

        # ENTITIES
        self.player1 = Entity (
            topleft = (10, 368),
            images_path = "../assets/img/miscellaneous/characters_models/character_blue.png",
            scale = 2.0
        )

        self.player2 = Entity (
            topleft = (658, 368),
            images_path = "../assets/img/miscellaneous/characters_models/character_green.png",
            scale = 2.0
        )
        self.player2.flip()
        
        # ADDING SPRITES TO INITIAL GROUPS
        self.buttons.add([self.ground])
        self.texts.add([])
        self.entities.add([self.player1, self.player2])

        # MUSIC
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.load("../assets/audio/music/battle_theme.mp3")
        pygame.mixer.music.play(-1)

    def next_window(self):
        pass

    def previous_window(self):
        pass