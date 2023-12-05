from .jelly_ui.sprites.Entity import Entity


class GroundEntity(Entity):
    def __init__(self, topleft, images_path, scale: float = 1):
        super().__init__(topleft, images_path, scale)

