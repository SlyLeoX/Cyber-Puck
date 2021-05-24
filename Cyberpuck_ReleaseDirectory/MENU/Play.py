import pygame
from MENU.Application import Application

from CORE.main_junction import core

#this class file served to activate the game with the selected paramters previously
class Play(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.player_parameters = [["PLAYER1","Sanic", "keyboard1"],
                         ["0COM2", "Alexander", "keyboard2"]]

        self.game_parameters = ["score_3", "metal1"]

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            core(self.game.system_parameters, self.player_parameters, self.game_parameters)
            pygame.mixer.music.load(r'MENU\midnight-ride-01a.wav')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        self.run_display = False
