import pygame
import sys

from CORE.classPlayer import PlayerType


class AiType(PlayerType):

    def __init__(self, x, y, infopack, game, number=-1):

        PlayerType.__init__(self, x, y, infopack)

        # The input parameters are a pain to manage, so the IA's level 'x' shall appear as "xCOMn" in inputs.
        self.level = int(infopack[0][0])

        self.max_speed -= 2
        # self.map = "0"

    def get_object_pos_x(self, object):
        return object.true_pos[0]

    def get_object_pos_y(self, object):
        return object.true_pos[1]

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
    def ia_choice_lvl0(self,game):
        # Rappel: "game.base entities[0]" designe l'objet "Puck" 100% des cas.
        puck_pos_x = self.get_object_pos_x(game.base_entities[0])
        puck_pos_y = self.get_object_pos_y(game.base_entities[0])
        ai_pos_x = self.get_object_pos_x(game.base_entities[2])
        ai_pos_y = self.get_object_pos_y(game.base_entities[2])
        #puck_speed = self.get_puck_speed(game.base_entities[0])
        #opponent_speed = self.get_opponent_speed(game.players)

        if puck_pos_y < ai_pos_y:
            self.current_inputs[1] = -0.75

        if puck_pos_y > ai_pos_y:
            self.current_inputs[1] = 0.75

        if puck_pos_x < ai_pos_x:
            self.current_inputs[0] = -0.75

        if puck_pos_x > ai_pos_x:
            self.current_inputs[0] = 0.75
