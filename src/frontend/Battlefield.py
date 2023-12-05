import pygame
import os
import random

from .jelly_ui.Window import Window
from .jelly_ui.sprites.Button import Button
from .jelly_ui.sprites.Text import Text
from .jelly_ui.sprites.Entity import Entity
from backend.Main import Main


class Battlefield(Window):
    def __init__(self, game):
        super().__init__(game)
        self.background_color = (255, 255, 255)

        # INIT BACKEND
        self.game.backend = Main(
            start_positions=self.game.possible_start_positions[
                self.game.nb_players - 1
            ],
            grid_dim=self.game.grid_dim,
            max_t=10,
        )

        # TEXTS

        # BUTTONS
        self.ground = Button(
            (0, 400), None, None, background_color=(0, 0, 0), rect_size=(700, 100)
        )

        # ENTITIES
        path = "../assets/img/miscellaneous/characters_models"
        skins = [
            os.path.join(path, s)
            for s in os.listdir(path)
            if os.path.isfile(os.path.join(path, s))
        ]
        random.shuffle(skins)
        players_entities = [
            Entity(
                topleft=(
                    self.game.backend.players[i].position.x,
                    self.game.backend.players[i].position.y,
                ),
                images_path=skins.pop(),
                scale=2.0,
            )
            for i in range(self.game.nb_players)
        ]
        players_entities[1].flip()  # TODO add players/entities direction

        # ADDING SPRITES TO INITIAL GROUPS
        self.buttons.add([self.ground])
        self.texts.add([])
        self.entities.add(players_entities)

        # MUSIC
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.load("../assets/audio/music/battle_theme.mp3")
        pygame.mixer.music.play(-1)

        # RUN BACKEND
        self.game.backend.start()

    def next_window(self):
        pass

    def previous_window(self):
        pass
