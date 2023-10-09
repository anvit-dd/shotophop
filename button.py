import pygame


class Button:
    def __init__(self, screen: None, color: str, x: float, y: float, button_x: int, button_y: int, scale: int,
                 text: str = None, text_size: int = 30, is_color_button=True, image_button=None):
        self.rect = pygame.draw.rect(screen, color, (x, y, button_x, button_y), scale)
        self.text = text
        self.button_x = button_x
        self.button_y = button_y
        self.color = color
        self.is_color_button = is_color_button
        self.clicked = False
        self.screen = screen
        self.x = x
        self.y = y
        self.action = False
        self.text_size = text_size
        self.image_button = image_button
        self.draw()

    def draw(self):

        if self.image_button is None:
            font = pygame.font.Font(None, self.text_size)
            text_render = font.render(self.text, True, "White")
            text_x = self.rect.x + (self.button_x - text_render.get_width()) // 2
            text_y = self.rect.y + (self.button_y - text_render.get_height()) // 2
            self.screen.blit(text_render, (text_x, text_y))
        else:
            self.screen.blit(self.image_button, (self.x, self.y))
        pygame.display.update()

    def click(self, pos):
        self.action = False
        if self.rect.collidepoint(pos):
            if pygame.MOUSEBUTTONUP and self.clicked is False:
                self.clicked = True
                self.action = True
        self.clicked = False
        return self.action

    def is_color(self):
        if self.is_color_button:
            return self.color
