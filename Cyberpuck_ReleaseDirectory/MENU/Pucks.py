import pygame
from MENU.Application import Application

class Pucks(Application):
    def __init__(self, game):
        Application.__init__(self, game)

        self.width, self.height = 1366, 768
        self.display = pygame.Surface((self.width,self.height))

        self.puck1 = pygame.image.load('MENU\puck1.png')
        self.puck2 = pygame.image.load('MENU\puck2.png')
        self.back = pygame.image.load('MENU\Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.move_cursor()
            self.game.background(self.back)

            self.game.draw_puck1(self.puck1)
            self.game.draw_puck2(self.puck2)

            self.game.draw_text_2('Pucks', 50, 300, 100)
            self.blit_screen()

    def move_cursor(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.collection
            self.play_sfx(r'MENU\book-cover-close-01.wav')
            self.run_display = False
