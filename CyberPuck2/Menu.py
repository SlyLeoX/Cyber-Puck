import pygame
from CyberPuck2.Slt_Menu import Slt_Menu
from Multilingual import multiL, currL

class Menu:

    def __init__(self, application, *groups):
        self.colors = dict(normal=(200, 200, 0), survol=(0, 200, 200))
        font = pygame.font.SysFont('Helvetica', 30, bold=True)
        items = ((multiL[currL]['Story'], application.story),
                 (multiL[currL]['Versus'], application.versus),
                 (multiL[currL]['Collection'], application.collection),
                 (multiL[currL]['Settings'], application.settings),
                 (multiL[currL]['Credit'], application.credit),
                 (multiL[currL]['Quit'], application.quit))
        x = 1366 / 2
        y = 100
        self.buttons = []
        self.image = pygame.image.load("logo_test.png")
        pygame.display.set_icon(self.image)
        for text, cmd in items:
            mb = Slt_Menu(text, self.colors['normal'], font, x, y, 200, 50, cmd)
            self.buttons.append(mb)
            y += 120
            for groupe in groups:
                groupe.add(mb)

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