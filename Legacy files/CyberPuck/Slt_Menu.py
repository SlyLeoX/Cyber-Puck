import pygame

width = 1366
height = 768

class Slt_Menu(pygame.sprite.Sprite):

    def __init__(self, text, color, font, x, y, width, height, command):
        super().__init__()
        self._command = command

        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.text = font.render(text, True, (0, 0, 0))
        self.rectText = self.text.get_rect()
        self.rectText.center = (width / 2, height / 2)

        #self.dessiner(color)


    def dessiner(self, color):
        self.image.fill(color)
        self.image.blit(self.text, self.rectText)


    def executerCommande(self):
        self._command()