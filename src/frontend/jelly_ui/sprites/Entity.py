import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, topleft, images_path, scale: float = 1.0):
        super().__init__()
        # IMAGES
        self.scale = scale
        images_path = images_path if isinstance(images_path, list) else [images_path]
        self.images = [
            pygame.transform.scale_by(
                pygame.image.load(image_path), (self.scale, self.scale)
            )
            for image_path in images_path
        ]
        self.topleft = topleft
        self.current_image_index = 0
        self.update_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft=topleft)

    def update(self):
        pass

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
