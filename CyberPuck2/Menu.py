import pygame
from CyberPuck2.Slt_Menu import Slt_Menu
from CyberPuck2.Multilingual import transL, setL

class Menu:

    def addSpriteMenu(self, x, y , text, cmd):
        font = pygame.font.SysFont('Helvetica', 29, bold=True)
        mb = Slt_Menu(text, self.colors['normal'], font, x, y, 225, 50, cmd)
        self.buttons.append(mb)
        for groupe in self.groups:
            groupe.add(mb)

    def setFr(self):
        setL("fr")
        self.showMenu()

    def setDe(self):
        setL("de")
        self.showMenu()

    def setEs(self):
        setL("es")
        self.showMenu()

    def setEn(self):
        setL("en")
        self.showMenu()

    def showMenu(self):
        for groupe in self.groups:
            groupe.empty()  #pour éviter les superpositions de sprites
        items = ((transL('Story'), self.application.story),
                 (transL('Versus'), self.application.versus),
                 (transL('Collection'), self.application.collection),
                 (transL('Settings'), self.application.settings),
                 (transL('Credit'), self.application.credit),
                 (transL('Quit'), self.application.quit))
        self.colors = dict(normal=(200, 200, 0), survol=(0, 200, 200))

        x = 1366 / 2
        y = 100
        self.buttons = []

        self.addSpriteMenu(1*x//5, y, "Français", self.setFr)
        self.addSpriteMenu(3*x//5, y, "Deutsch", self.setDe)
        self.addSpriteMenu(7*x//5, y, "Español", self.setEs)
        self.addSpriteMenu(9*x//5, y, "English", self.setEn)

        for text, cmd in items:
            self.addSpriteMenu(x, y, text, cmd)
            y += 120

    def __init__(self, application, *groups):
        self.groups = groups
        self.application = application

        self.image = pygame.image.load("logo_test.png")
        pygame.display.set_icon(self.image)

        self.showMenu()


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