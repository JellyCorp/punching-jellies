from .jelly_ui.sprites.Entity import Entity


class PlayerEntity(Entity):
    def __init__(self, topleft, images_path, player, scale: float = 1):
        super().__init__(topleft, images_path, scale)

        self.player = player

    def update(self):
        self.topleft = (self.player.position.x, self.player.position.y)
        super().update()
