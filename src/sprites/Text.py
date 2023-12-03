import pygame


class Text(pygame.sprite.Sprite):
    def __init__(
        self,
        topleft: (int, int),
        text: str,
        font: pygame.font.Font,
        color: (int, int, int) = (0, 0, 0),
        antialiazing: bool = True,
    ):
        super().__init__()

        self.image = font.render(text, antialiazing, color)
        self.rect = self.image.get_rect(topleft=topleft)
