import pygame
from CyberPuck2.Menu import Menu
from CyberPuck2.Story import Story
from CyberPuck2.Versus import Versus
from CyberPuck2.Collection import Collection
from CyberPuck2.Settings import Settings
from CyberPuck2.Credit import Credit

width = 1366
height = 768

class Application:

    def __init__(self):
        pygame.init()
        self.start()
        pygame.display.set_caption("Cyber Puck")

        self.fenetre = pygame.display.set_mode((width, height))
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

        image = pygame.image.load('Gear.png')
        self.fenetre.blit(image, (0, 0))


    def start(self):
        try:
            self.screen.destroy()
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        self.start()
        self.screen = Menu(self, self.groupeGlobal)


    def story(self):
        self.start()
        self.screen = Story(self)

    def versus(self):
        self.start()
        self.screen = Versus(self)

    def collection(self):
        self.start()
        self.screen = Collection(self)

    def settings(self):
        self.start()
        self.screen = Settings(self)

    def credit(self):
        self.start()
        self.screen = Credit(self)


    def quit(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
                return


        #self.start()
        self.screen.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()