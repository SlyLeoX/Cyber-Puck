import pygame
from MENU.Application import Application

from CORE.main_junction import core


class Selection(Application):
    def __init__(self, game):
        Application.__init__(self, game)

        self.perso10x, self.perso10y = self.midw - 400, self.midh - 100
        self.perso20x, self.perso20y = self.midw - 400, self.midh
        self.perso30x, self.perso30y = self.midw - 400, self.midh + 100
        self.perso40x, self.perso40y = self.midw - 400, self.midh + 200
        self.perso50x, self.perso50y = self.midw - 400, self.midh + 300
        self.perso11x, self.perso11y = self.midw + 400, self.midh - 100
        self.perso21x, self.perso21y = self.midw + 400, self.midh
        self.perso31x, self.perso31y = self.midw + 400, self.midh + 100
        self.perso41x, self.perso41y = self.midw + 400, self.midh + 200
        self.perso51x, self.perso51y = self.midw + 400, self.midh + 300
        self.playx, self.playy = self.midw, self.midh

        self.state = "Sanic"
        self.cursor_rect.midtop = (self.perso10x + self.offset, self.perso10y)

        self.back = pygame.image.load('MENU\Back_Menu.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            print(self.state)
            self.game.check_events()
            self.check_input()
            self.check_input2()
            self.check_input3()
            self.game.background(self.back)
            self.game.draw_text_2('Selection', 50, 250, 100)
            self.game.draw_text_3("P1 character", 40, self.midw - 400, self.midh - 200)
            self.game.draw_text_3("P2 character", 40, self.midw + 400, self.midh - 200)
            self.game.draw_text("Sanic", 40, self.perso10x, self.perso10y)
            self.game.draw_text("Alexander", 40, self.perso20x, self.perso20y)
            self.game.draw_text("Harry", 40, self.perso30x, self.perso30y)
            self.game.draw_text("Remilia", 40, self.perso40x, self.perso40y)
            self.game.draw_text("Sakuya", 40, self.perso50x, self.perso50y)
            self.game.draw_text("Sanic", 40, self.perso11x, self.perso11y)
            self.game.draw_text("Alexander", 40, self.perso21x, self.perso21y)
            self.game.draw_text("Harry", 40, self.perso31x, self.perso31y)
            self.game.draw_text("Remilia", 40, self.perso41x, self.perso41y)
            self.game.draw_text("Sakuya", 40, self.perso51x, self.perso51y)
            self.game.draw_text_2("Play", 40, self.playx, self.playy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.S_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.cursor_rect.midtop = (self.perso20x + self.offset, self.perso20y)
                self.state = 'Alexander'
            elif self.state == 'Alexander':
                self.cursor_rect.midtop = (self.perso30x + self.offset, self.perso30y)
                self.state = 'Harry'
            elif self.state == 'Harry':
                self.cursor_rect.midtop = (self.perso40x + self.offset, self.perso40y)
                self.state = 'Mephiles'
            elif self.state == 'Mephiles':
                self.cursor_rect.midtop = (self.perso50x + self.offset, self.perso50y)
                self.state = 'Leowenex'
            elif self.state == 'Leowenex':
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = 'Play'
            elif self.state == 'Play':
                self.cursor_rect.midtop = (self.perso10x + self.offset, self.perso10y)
                self.state = 'Sanic'

        elif self.game.Z_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = 'Play'
            elif self.state == 'Alexander':
                self.cursor_rect.midtop = (self.perso10x + self.offset, self.perso10y)
                self.state = 'Sanic'
            elif self.state == 'Harry':
                self.cursor_rect.midtop = (self.perso20x + self.offset, self.perso20y)
                self.state = 'Alexander'
            elif self.state == 'Mephiles':
                self.cursor_rect.midtop = (self.perso30x + self.offset, self.perso30y)
                self.state = 'Harry'
            elif self.state == 'Leowenex':
                self.cursor_rect.midtop = (self.perso40x + self.offset, self.perso40y)
                self.state = 'Mephiles'
            elif self.state == 'Play':
                self.cursor_rect.midtop = (self.perso50x + self.offset, self.perso50x)
                self.state = 'Leowenex'

        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.versus
            self.play_sfx(r'MENU\book-cover-close-01.wav')
            self.run_display = False

    def move_cursor2(self):
        if self.game.DOWN_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.cursor_rect.midtop = (self.perso21x + self.offset, self.perso21y)
                self.state = 'Alexander'
            elif self.state == 'Alexander':
                self.cursor_rect.midtop = (self.perso31x + self.offset, self.perso31y)
                self.state = 'Harry'
            elif self.state == 'Harry':
                self.cursor_rect.midtop = (self.perso41x + self.offset, self.perso41y)
                self.state = 'Mephiles'
            elif self.state == 'Mephiles':
                self.cursor_rect.midtop = (self.perso51x + self.offset, self.perso51y)
                self.state = 'Leowenex'
            elif self.state == 'Leowenex':
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = 'Play'
            elif self.state == 'Play':
                self.cursor_rect.midtop = (self.perso11x + self.offset, self.perso11y)
                self.state = 'Sanic'

        elif self.game.UP_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = 'Play'
            elif self.state == 'Alexander':
                self.cursor_rect.midtop = (self.perso11x + self.offset, self.perso11y)
                self.state = 'Sanic'
            elif self.state == 'Harry':
                self.cursor_rect.midtop = (self.perso21x + self.offset, self.perso21y)
                self.state = 'Alexander'
            elif self.state == 'Mephiles':
                self.cursor_rect.midtop = (self.perso31x + self.offset, self.perso31y)
                self.state = 'Harry'
            elif self.state == 'Leowenex':
                self.cursor_rect.midtop = (self.perso41x + self.offset, self.perso41y)
                self.state = 'Mephiles'
            elif self.state == 'Play':
                self.cursor_rect.midtop = (self.perso51x + self.offset, self.perso51y)
                self.state = 'Leowenex'

        elif self.game.BACK_KEY:
            self.game.curr_menu = self.game.versus
            self.play_sfx(r'MENU\book-cover-close-01.wav')
            self.run_display = False

    def check_input(self):
        self.move_cursor()
        if self.game.TAB_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.game.player_parameters[0][1] = "Sanic"
            elif self.state == 'Alexander':
                self.game.player_parameters[0][1] = "Alexander"
            elif self.state == 'Harry':
                self.game.player_parameters[0][1] = "Harry"
            elif self.state == 'Mephiles':
                self.game.player_parameters[0][1] = "Remilia"
            elif self.state == 'Leowenex':
                self.game.player_parameters[0][1] = "Sakuya"
            self.run_display = False

    def check_input2(self):
        self.move_cursor2()
        if self.game.START_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Sanic':
                self.game.player_parameters[1][1] = "Sanic"
            elif self.state == 'Alexander':
                self.game.player_parameters[1][1] = "Alexander"
            elif self.state == 'Harry':
                self.game.player_parameters[1][1] = "Harry"
            elif self.state == 'Mephiles':
                self.game.player_parameters[1][1] = "Remilia"
            elif self.state == 'Leowenex':
                self.game.player_parameters[1][1] = "Sakuya"
            self.run_display = False

    def check_input3(self):
        if self.game.START_KEY or self.game.TAB_KEY:
            if self.state == 'Play':
                # self.game.curr_menu = self.game.play
                core(self.game.system_parameters, self.game.player_parameters, self.game.game_parameters)
                pygame.mixer.music.load(r'MENU\midnight-ride-01a.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
        self.run_display = False