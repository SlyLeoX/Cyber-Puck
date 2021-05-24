import pygame
import winsound
from MENU.Application import Application

class Characters(Application):
    def __init__(self, game):
        Application.__init__(self, game)

        self.width, self.height = 1366, 768
        self.display = pygame.Surface((self.width,self.height))

        self.perso1 = pygame.image.load('MENU\perso1.png')
        self.perso2 = pygame.image.load('MENU\perso2.png')
        self.back = pygame.image.load('MENU\Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.move_cursor()
            self.game.background(self.back)

            self.game.draw_perso1(self.perso1)
            self.game.draw_perso2(self.perso2)

            self.game.draw_text_3('Alexander', 25, 525, 600)
            self.game.draw_text_3('Harry', 25, 925, 600)

            self.game.draw_text_2('Characters', 50, 300, 100)
            self.blit_screen()

    def move_cursor(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.collection
            self.play_sfx(r'MENU\book-cover-close-01.wav')
            self.run_display = False
