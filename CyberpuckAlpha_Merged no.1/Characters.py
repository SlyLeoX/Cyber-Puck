import pygame
import winsound
from Application import Application

class Characters(Application):
    def __init__(self, game):
        Application.__init__(self, game)

        self.width, self.height = 1366, 768
        self.display = pygame.Surface((self.width,self.height))

        self.perso1 = pygame.image.load('perso1.png')
        self.perso2 = pygame.image.load('perso2.png')
        self.back = pygame.image.load('Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.background(self.back)

            self.game.draw_perso1(self.perso1)
            self.game.draw_perso2(self.perso2)

            self.game.draw_text_3('Alexander', 25, 525, 600)
            self.game.draw_text_3('Harry', 25, 925, 600)

            self.game.draw_text_2('Characters', 50, 300, 100)
            self.blit_screen()