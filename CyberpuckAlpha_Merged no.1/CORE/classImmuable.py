import pygame

class goalType:
    def __init__(self, x, y, texture=r"CORE\ressources\misc\goals.gif"):
        self.tex = pygame.image.load(texture).convert()
        self.rect = self.tex.get_rect()
        self.rect2 = self.tex.get_rect()
        y_offset = 90

        self.rect.x = self.rect2.x = x
        self.rect.y = y - 100 + y_offset
        self.rect2.y = y + 100 + y_offset

        self.rectlist = [self.rect, self.rect2]