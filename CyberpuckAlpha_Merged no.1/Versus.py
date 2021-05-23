import pygame
from Application import Application

class Versus(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.state = "1 VS 1"
        self.mode1x, self.mode1y = self.midw + 100, self.midh - 100
        self.mode2x, self.mode2y = self.midw + 500, self.midh - 100
        self.pointsx, self.pointsy = self.midw + 100, self.midh + 40
        self.timex, self.timey = self.midw + 500, self.midh + 40
        self.nextx, self.nexty = self.midw, self.midh + 200

        self.back = pygame.image.load('Back_Menu.png')

        self.game.player_parameters = [["PLAYER1","Sanic", "keyboard1"],
                         ["0COM2", "Alexander", "keyboard2"]]

        self.game.game_parameters = ["score_3", "metal1"]

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
            self.game.draw_text_3("Game Mode", 40, self.midw - 400, self.mode1y)
            self.game.draw_text_3("Type of Game", 40, self.midw - 400, self.pointsy)
            self.game.draw_text_2("NEXT", 40, self.nextx, self.nexty + 25)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.play_sfx('button-3.wav')
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
                self.cursor_rect.midtop = (self.nextx + self.offset, self.nexty)
                self.state = 'NEXT'
            elif self.state == 'NEXT':
                self.cursor_rect.midtop = (self.mode1x + self.offset, self.mode1y)
                self.state = '1 VS 1'

        elif self.game.UP_KEY:
            self.play_sfx('button-3.wav')
            if self.state == '1 VS 1':
                self.cursor_rect.midtop = (self.nextx + self.offset, self.nexty)
                self.state = 'NEXT'
            elif self.state == '1 VS AI':
                self.cursor_rect.midtop = (self.mode1x + self.offset, self.mode1y)
                self.state = '1 VS 1'
            elif self.state == 'Points':
                self.cursor_rect.midtop = (self.mode2x + self.offset, self.mode2y)
                self.state = '1 VS AI'
            elif self.state == 'Time':
                self.cursor_rect.midtop = (self.pointsx + self.offset, self.pointsy)
                self.state = 'Points'
            elif self.state == 'NEXT':
                self.cursor_rect.midtop = (self.timex + self.offset, self.timey)
                self.state = 'Time'

        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.menu
            self.play_sfx('book-cover-close-01.wav')
            self.run_display = False

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            self.play_sfx('button-3.wav')
            if self.state == '1 VS 1':
                self.game.player_parameters[1][0] = "PLAYER2"
            elif self.state == '1 VS AI':
                self.game.player_parameters[1][0] = "0COM2"
            elif self.state == 'Points':
                self.game.game_parameters[0] = "score_3"
            elif self.state == 'Time':
                self.game.game_parameters[0] = "time_90"
            elif self.state == 'NEXT':
                self.game.curr_menu = self.game.selection
            self.run_display = False
