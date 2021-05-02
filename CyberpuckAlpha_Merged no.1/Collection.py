import pygame
import winsound
from Application import Application

class Collection(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.state = "Characters"
        self.persox, self.persoy = self.midw, self.midh - 100
        self.puckx, self.pucky = self.midw, self.midh + 180

        self.back = pygame.image.load('Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.background(self.back)
            self.game.draw_text_2('Collection', 50, 300, 100)
            self.game.draw_text("Characters", 40, self.persox, self.persoy)
            self.game.draw_text("Pucks", 40, self.puckx, self.pucky)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == 'Characters':
                self.cursor_rect.midtop = (self.persox + self.offset, self.persoy)
                self.state = 'Pucks'
            elif self.state == 'Pucks':
                self.cursor_rect.midtop = (self.puckx + self.offset, self.pucky)
                self.state = 'Characters'


        elif self.game.UP_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == 'Characters':
                self.cursor_rect.midtop = (self.puckx + self.offset, self.pucky)
                self.state = 'Pucks'
            elif self.state == 'Pucks':
                self.cursor_rect.midtop = (self.persox + self.offset, self.persoy)
                self.state = 'Characters'

        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.menu
            winsound.PlaySound('book-cover-close-01.wav', winsound.SND_FILENAME)
            self.run_display = False


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Characters':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                #self.game.playing = True
                #self.game.curr_menu = self.game.characters
                self.game.curr_menu = self.game.pucks
            elif self.state == 'Pucks':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                #self.game.curr_menu = self.game.quit
                self.game.curr_menu = self.game.characters
            self.run_display = False
