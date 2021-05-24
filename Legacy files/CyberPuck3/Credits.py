import pygame
import winsound
from CyberPuck3.Application import Application

class Credits(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.back = pygame.image.load('Back_Menu.png')
        self.logo_efrei = pygame.image.load('logo_efrei.png')

        self.name1x, self.name1y = self.midw + 300, self.midh - 100
        self.name2x, self.name2y = self.midw + 300, self.midh - 30
        self.name3x, self.name3y = self.midw + 300, self.midh + 40
        self.name4x, self.name4y = self.midw + 300, self.midh + 110
        self.name5x, self.name5y = self.midw + 300, self.midh + 180
        self.name6x, self.name6y = self.midw + 300, self.midh + 250

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.menu
                winsound.PlaySound('book-cover-close-01.wav', winsound.SND_FILENAME)
                self.run_display = False
            self.game.background(self.back)
            self.game.draw_logo_efrei(self.logo_efrei)
            self.game.draw_text_3('Credits', 50, 250, 100)
            self.game.draw_text_2('Members', 50, self.midw + 300, self.midh -200)
            self.game.draw_text('Antoine Craipeau', 40, self.name1x, self.name1y)
            self.game.draw_text('Emma Deste', 40, self.name2x, self.name2y)
            self.game.draw_text('Romeo Gennari', 40, self.name3x, self.name3y)
            self.game.draw_text('Kevin Op', 40, self.name4x, self.name4y)
            self.game.draw_text('Leo Petit', 40, self.name5x, self.name5y)
            self.game.draw_text('Quentin Rault', 40, self.name6x, self.name6y)
            self.blit_screen()