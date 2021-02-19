import pygame

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
        #self.TextCredit()
        self.ImageCredit()

        #self.fenetre = pygame.display.set_mode((width, height))
        #image = pygame.image.load('Gear.png')
        #self.fenetre.blit(image, (0, 0))

        self.rectTexte = self.text.get_rect()
        self.rectTexte.center = (width / 2, height / 2)
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

    def TextCredit(self):
        TextDisplay = pygame.display.set_mode((width, height))

        color1 = (0, 0, 200)
        color2 = (255, 255, 255)
        color3 = (0, 200, 0)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('L1 INT', True, color1)
        text2 = font.render('Promo 2020 - 2021', True, color1)

        nom1 = font.render('Antoine Craipeau', True, color3)
        nom2 = font.render('Emma Desté', True, color3)
        nom3 = font.render('Roméo Gennari', True, color3)
        nom4 = font.render('Kevin Op', True, color3)
        nom5 = font.render('Léo Petit', True, color3)
        nom6 = font.render('Quentin Rault', True, color3)

        textRect = text.get_rect()
        text2Rect = text2.get_rect()

        nom1Rect = nom1.get_rect()
        nom2Rect = nom2.get_rect()
        nom3Rect = nom3.get_rect()
        nom4Rect = nom4.get_rect()
        nom5Rect = nom5.get_rect()
        nom6Rect = nom6.get_rect()


        textRect.center = (200, 100)
        text2Rect.center = (200, 200)

        nom1Rect.center = (1000, 100)
        nom2Rect.center = (1000, 200)
        nom3Rect.center = (1000, 300)
        nom4Rect.center = (1000, 400)
        nom5Rect.center = (1000, 500)
        nom6Rect.center = (1000, 600)

        while True:
            TextDisplay.fill(color2)

            TextDisplay.blit(text, textRect)
            TextDisplay.blit(text2, text2Rect)

            pygame.display.update()

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

        nom1Rect.center = (900, 200)
        nom2Rect.center = (900, 300)
        nom3Rect.center = (900, 400)
        nom4Rect.center = (900, 500)
        nom5Rect.center = (900, 600)
        nom6Rect.center = (900, 700)

        while True:
            ImageDisplay.fill(color)
            ImageDisplay.blit(Image, (0, 0))

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
                self.TextCredit()
                self.ImageCredit()
                break

    def destroy(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)