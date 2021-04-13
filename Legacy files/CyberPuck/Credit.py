import pygame
from CyberPuck.Trash import Trash

width = 1366
height = 768

class Credit:

    def __init__(self, game):
        self._fenetre = game.fenetre
        game.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self.TextColor = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.ImageCredit()

        self.rectTexte = self.text.get_rect()
        self.rectTexte.center = (width / 2, height / 2)


    def ImageCredit(self):
        ImageDisplay = pygame.display.set_mode((width, height))

        color = (255, 255, 255)
        color1 = (0, 0, 200)
        color2 = (0, 200, 0)

        Image = pygame.image.load('logo_efrei.png')

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('L1 INT', True, color1)
        text2 = font.render('Promo 2020 - 2021', True, color1)

        nom1 = font.render('Antoine Craipeau', True, color2)
        nom2 = font.render('Emma Desté', True, color2)
        nom3 = font.render('Roméo Gennari', True, color2)
        nom4 = font.render('Kevin Op', True, color2)
        nom5 = font.render('Léo Petit', True, color2)
        nom6 = font.render('Quentin Rault', True, color2)

        text_rect = text.get_rect()
        text2_rect = text2.get_rect()

        nom1Rect = nom1.get_rect()
        nom2Rect = nom2.get_rect()
        nom3Rect = nom3.get_rect()
        nom4Rect = nom4.get_rect()
        nom5Rect = nom5.get_rect()
        nom6Rect = nom6.get_rect()

        text_rect.center = (100, 100)
        text2_rect.center = (200, 180)

        nom1Rect.center = (900, 150)
        nom2Rect.center = (900, 250)
        nom3Rect.center = (900, 350)
        nom4Rect.center = (900, 450)
        nom5Rect.center = (900, 550)
        nom6Rect.center = (900, 650)

        while True:
            ImageDisplay.fill(color)
            ImageDisplay.blit(Image, (0, 250))

            ImageDisplay.blit(text, text_rect)
            ImageDisplay.blit(text2, text2_rect)

            ImageDisplay.blit(nom1, nom1Rect)
            ImageDisplay.blit(nom2, nom2Rect)
            ImageDisplay.blit(nom3, nom3Rect)
            ImageDisplay.blit(nom4, nom4Rect)
            ImageDisplay.blit(nom5, nom5Rect)
            ImageDisplay.blit(nom6, nom6Rect)

            pygame.display.update()

    def update(self, events):
        self._fenetre.blit(self.text, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.ImageCredit()
                break

    def back(self):
        screen = pygame.display.set_mode((width, height))
        color = (255, 255, 255)

        smallfont = pygame.font.Sysfont('Corbel', 35)
        text = smallfont.render('back', True, color)

        while True:

            for ev in pygame.event.get():
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1]
                    pygame.quit()

    def destroy(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)