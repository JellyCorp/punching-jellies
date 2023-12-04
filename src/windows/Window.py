from abc import ABC, abstractmethod
import pygame


class Window(ABC):
    def __init__(self, game):
        self.game = game
        self.texts = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.background = None
        self.background_color = (0, 0, 0)

    @abstractmethod
    def previous_window(self):
        pass

    @abstractmethod
    def next_window(self):
        pass

    def update(self, pos):
        cursor = pygame.SYSTEM_CURSOR_ARROW

        # logical
        for button in self.buttons:
            if button.update(pos):
                cursor = pygame.SYSTEM_CURSOR_HAND

        for entity in self.entities:
            entity.update()

        # background
        self.game.screen.fill(self.background_color)
        if self.background is not None:
            background = pygame.image.load(self.background)
            self.game.screen.blit(background, (0, 0))

        # groups
        self.buttons.draw(self.game.screen)
        self.texts.draw(self.game.screen)
        self.entities.draw(self.game.screen)

        return cursor

    def handle_event(self, event):
        for button in self.buttons:
            button_result = button.handle_event(event)
            if button_result is not None:
                return button_result
