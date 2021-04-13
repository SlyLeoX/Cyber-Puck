import pygame
import sys

from CyberpuckCore_mod2.classPlayer import PlayerType


class AiType(PlayerType):

    def __init__(self, x, y, infopack, number=-1):

        PlayerType.__init__(self, x, y, infopack)

    def get_puck_pos(self,puck):
        return puck.true_pos

    def get_puck_speed(self,puck):
        return puck.speed

    def get_opponent_speed(self,players):
        for player in players:
            # The players objects have a unique number given at launch, kinda allowing to identify these easily.
            if player.number != self.number:
                return player.true_pos

        # If at this point nothing has been returned yet, something went wrong :/
        return 0

    # Fonction principale appelée par le loop:
    def ia_choice(self,game):
        # Rappel: "game.base entities[0]" designe l'objet "Puck" 100% des cas.
        puck_pos = self.get_puck_pos(game.base_entities[0])
        puck_speed = self.get_puck_speed(game.base_entities[0])
        opponent_speed = self.get_opponent_speed(game.players)

