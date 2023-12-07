import pygame

from .jelly_ui.sprites.Entity import Entity

class PlayerEntity(Entity):
    def __init__(self, topleft, images_path, player, scale: float = 1):
        super().__init__(topleft, images_path, scale)
        self.player = player
        self.look_right = self.player.look_right

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        self.topleft = (self.player.position.x, self.player.position.y)
        if (self.look_right != self.player.look_right):
            self.flip()
            self.look_right = not self.look_right
        super().update()
