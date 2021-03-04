import pygame

class goals:
    def __init__(self, x, y, texture="Goal.jpg"):
        self.tex = pygame.image.load(texture).convert()
        self.rect = self.tex.get_rect()
        self.rect2 = self.tex.get_rect()

        self.rect.x = self.rect2.x = x
        self.rect.y = y-30
        self.rect2.y = 
