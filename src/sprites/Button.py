import pygame


class Button(pygame.sprite.Sprite):
    def __init__(
        self,
        topleft,
        callback=None,
        image_path=None,
        image_hover_path=None,
        selected=False,
        disable=False,
        wider_touch=False,
        scale: float = 1.0,
        background_color = (255, 255, 255),
        rect_size = (0, 0),
        **kwargs
    ):
        super().__init__()

        # STATE
        self.selected = selected

        # CALLBACK
        self.callback = callback
        self.kwargs = kwargs
        self.disable = disable
        self.wider_touch = wider_touch

        # IMAGES
        self.scale = scale
        self.default_image = (
            None
            if image_path is None
            else 
            pygame.transform.scale_by(pygame.image.load(image_path), (self.scale, self.scale))
        )
        self.image_hover = (
            None
            if image_hover_path is None
            else pygame.transform.scale_by(
                pygame.image.load(image_hover_path), (self.scale, self.scale)
            )
        )

        # DEFAULTS
        self.topleft = topleft
        if self.default_image is not None:
            self.image = self.default_image
        else:
            self.image = pygame.Surface(size=rect_size)
            self.image.fill(background_color)
        self.rect = self.image.get_rect(topleft=topleft)

    def set_default_image(self, image_path):
        self.default_image = pygame.transform.scale_by(
            pygame.image.load(image_path), (self.scale, self.scale)
        )
        self.rect = self.image.get_rect(topleft=self.topleft)

    def set_hover_image(self, image_path):
        self.image_hover = pygame.transform.scale_by(
            pygame.image.load(image_path), (self.scale, self.scale)
        )

    def update(self, pos):  # TODO create a toggle state var
        hover = self.hover(pos)
        if self.selected or hover and self.image_hover is not None:
            self.image = self.image_hover
        elif not self.selected and self.image != self.default_image and self.default_image is not None:
            self.image = self.default_image

        return hover

    def handle_event(self, event):
        if (
            not self.disable and self.callback is not None
            and event.type == pygame.MOUSEBUTTONDOWN
            and (self.rect.collidepoint(event.pos) or self.wider_touch)
        ):
            self.callback() if not self.kwargs else self.callback(self.kwargs)

    def hover(self, mouse_pos):
        hover = False
        if not self.disable and (self.rect.collidepoint(mouse_pos) or self.wider_touch):
            hover = True

        return hover
