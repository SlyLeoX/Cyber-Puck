import pygame
import winsound
from CyberPuck3.Application import Application
from CyberpuckCore_mod2.Main_game import Main_game

class Versus(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.state = "1 VS 1"
        self.mode1x, self.mode1y = self.midw + 100, self.midh - 100
        self.mode2x, self.mode2y = self.midw + 500, self.midh - 100
        self.pointsx, self.pointsy = self.midw + 100, self.midh + 40
        self.timex, self.timey = self.midw + 500, self.midh + 40
        self.powerx, self.powery = self.midw + 100, self.midh + 180
        self.no_powerx, self.no_powery = self.midw + 500, self.midh + 180

        self.back = pygame.image.load('Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.background(self.back)
            self.game.draw_text_2('Versus', 50, 250, 100)
            self.game.draw_text("1 VS 1", 40, self.mode1x, self.mode1y)
            self.game.draw_text("1 VS AI", 40, self.mode2x, self.mode2y)
            self.game.draw_text("Points", 40, self.pointsx, self.pointsy)
            self.game.draw_text("Time", 40, self.timex, self.timey)
            self.game.draw_text("Enabled", 40, self.powerx, self.powery)
            self.game.draw_text("Disabled", 40, self.no_powerx, self.no_powery)
            self.game.draw_text_3("Game Mode", 40, self.midw - 400, self.mode1y)
            self.game.draw_text_3("Type of Game", 40, self.midw - 400, self.pointsy)
            self.game.draw_text_3("Super Power", 40, self.midw - 400, self.powery)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == '1 VS 1':
                self.cursor_rect.midtop = (self.mode2x + self.offset, self.mode2y)
                self.state = '1 VS AI'
            elif self.state == '1 VS AI':
                self.cursor_rect.midtop = (self.pointsx + self.offset, self.pointsy)
                self.state = 'Points'
            elif self.state == 'Points':
                self.cursor_rect.midtop = (self.timex + self.offset, self.timey)
                self.state = 'Time'
            elif self.state == 'Time':
                self.cursor_rect.midtop = (self.powerx + self.offset, self.powery)
                self.state = 'Enabled'
            elif self.state == 'Enabled':
                self.cursor_rect.midtop = (self.no_powerx + self.offset, self.no_powery)
                self.state = 'Disabled'
            elif self.state == 'Disabled':
                self.cursor_rect.midtop = (self.mode1x + self.offset, self.mode1y)
                self.state = '1 VS 1'

        elif self.game.UP_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == '1 VS 1':
                self.cursor_rect.midtop = (self.no_powerx + self.offset, self.no_powery)
                self.state = 'Disabled'
            elif self.state == '1 VS AI':
                self.cursor_rect.midtop = (self.mode1x + self.offset, self.mode1y)
                self.state = '1 VS 1'
            elif self.state == 'Points':
                self.cursor_rect.midtop = (self.mode2x + self.offset, self.mode2y)
                self.state = '1 VS 1'
            elif self.state == 'Time':
                self.cursor_rect.midtop = (self.pointsx + self.offset, self.pointsy)
                self.state = 'Points'
            elif self.state == 'Enabled':
                self.cursor_rect.midtop = (self.timex + self.offset, self.timey)
                self.state = 'Time'
            elif self.state == 'Disabled':
                self.cursor_rect.midtop = (self.powerx + self.offset, self.powery)
                self.state = 'Enabled'

        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.menu
            winsound.PlaySound('book-cover-close-01.wav', winsound.SND_FILENAME)
            self.run_display = False

    def main_game(self):
        g = Main_game(1)
        g.display_menu()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == '1 VS 1':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                #self.game.playing = True
                self.main_game()
                self.game.curr_menu = self.game.quit
            elif self.state == '1 VS AI':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            elif self.state == 'Points':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            elif self.state == 'Time':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            elif self.state == 'Enabled':
                #winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            elif self.state == 'Disabled':
                #winsound.PlaySound('button-4.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            self.run_display = False