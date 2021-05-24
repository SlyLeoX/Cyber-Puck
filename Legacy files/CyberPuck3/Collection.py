import pygame
import winsound
from CyberPuck3.Application import Application

class Collection(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.state = "Characters"
        self.persox, self.persoy = self.midw, self.midh - 100
        self.fieldx, self.fieldy = self.midw, self.midh + 40
        self.puckx, self.pucky = self.midw, self.midh + 180

        self.back = pygame.image.load('Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.background(self.back)
            self.game.draw_text_2('Collection', 50, 300, 100)
            self.game.draw_text_3("Characters", 40, self.persox, self.persoy)
            self.game.draw_text_3("Fields", 40, self.fieldx, self.fieldy)
            self.game.draw_text_3("Pucks", 40, self.puckx, self.pucky)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == 'Characters':
                self.cursor_rect.midtop = (self.persox + self.offset, self.persoy)
                self.state = 'Fields'
            elif self.state == 'Fields':
                self.cursor_rect.midtop = (self.fieldx + self.offset, self.fieldy)
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
                self.cursor_rect.midtop = (self.fieldx + self.offset, self.fieldy)
                self.state = 'Fields'
            elif self.state == 'Fields':
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
                self.game.curr_menu = self.game.quit
            elif self.state == 'Fields':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            elif self.state == 'Pucks':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            self.run_display = False