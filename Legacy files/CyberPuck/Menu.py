import pygame
from CyberPuck.Slt_Menu import Slt_Menu

width = 1366
height = 768

class Menu:

    def __init__(self, application, *groups):
        self.colors = dict(normal=(200, 200, 0), survol=(0, 200, 200))
        font = pygame.font.SysFont('Helvetica', 30, bold=True)
        items = (('Story', application.story), ('Versus', application.versus), ('Collection', application.collection),
                 ('Settings', application.settings), ('Credit', application.credit), ['Quit', application.quit])
        x = 300
        y = 120
        self.buttons = []
        self.image = pygame.image.load("logo_test.png")
        pygame.display.set_icon(self.image)
        for text, cmd in items:
            mb = Slt_Menu(text, self.colors['normal'], font, x, y, 200, 50, cmd)
            self.buttons.append(mb)
            y += 110
            for groupe in groups:
                groupe.add(mb)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.TextMenu()

    def TextMenu(self):
        fenetre = pygame.display.set_mode((width, height))

        color1 = (255, 0, 0)
        color2 = (255, 255, 255)

        font = pygame.font.Font('freesansbold.ttf', 130)
        font2 = pygame.font.Font('freesansbold.ttf', 60)

        text = font.render('CyberPuck', True, color1)
        name = font2.render('Username: ', True, color2)

        text_rect = text.get_rect()
        text_rect.center = (900, 200)

        name_rect = name.get_rect()
        name_rect.center = (750, 500)

        image = pygame.image.load('Gear.png')
        fenetre.blit(image, (0, 0))
        fenetre.blit(text, text_rect)
        fenetre.blit(name, name_rect)

        pygame.display.update()

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self.buttons:
            if bouton.rect.collidepoint(*posPointeur):
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                bouton.dessiner(self.colors['survol'])
                if clicGauche:
                    bouton.executerCommande()
                break
            else:
                bouton.dessiner(self.colors['normal'])
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def destroy(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)