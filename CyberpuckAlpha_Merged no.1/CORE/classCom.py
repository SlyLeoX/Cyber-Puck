import pygame
import sys
import numpy as np

from CORE.classPlayer import PlayerType


class AiType(PlayerType):

    def __init__(self, x, y, infopack, game, number=-1):

        PlayerType.__init__(self, x, y, infopack)

        # The input parameters are a pain to manage, so the IA's level 'x' shall appear as "xCOMn" in inputs.
        self.level = int(infopack[0][0])

        self.max_speed -= 2
        # self.map = "0"

        self.idea = 0
        self.target_x = 0
        self.target_y = 0

    def get_object_pos_x(self, object):
        return object.true_pos[0]

    def get_object_pos_y(self, object):
        return object.true_pos[1]

    def get_puck_speed(self, puck):
        return puck.speed

    def get_opponent_speed(self, players):
        for player in players:
            # The players objects have a unique number given at launch, kinda allowing to identify these easily.
            if player.number != self.number:
                return player.true_pos

        # If at this point nothing has been returned yet, something went wrong :/
        return 0

    def get_quickest_position(self, player_x_pos, player_y_pos, max_speed, ball_x_pos, ball_y_pos, ball_x_speed,
                              ball_y_speed):
        # We need to take into account the size of both the ball and the puck when checking the borders
        # Max speed in pix per frame
        catchable = False
        radius = 0
        # First we get the ball position that we can reach
        while not catchable:
            radius += max_speed
            ball_x_pos += ball_x_speed
            ball_y_pos += ball_y_speed
            if ball_y_pos > 768:
                ball_y_pos += 768 - ball_y_pos
                ball_y_speed *= -1
            if ball_x_pos > 1366:
                ball_x_pos += 1366 - ball_x_pos
                ball_x_speed *= -1
            if radius > ((ball_x_pos - player_x_pos) ** 2 + (ball_y_pos - player_y_pos) ** 2) ** (1 / 2):
                catchable = True
        # The following is from a time where I took a time to position, I don't think it's really necessary
        # But it's here if need be
        '''
        # Then we go where the ball will be 10 frames after that
        player_x_pos, player_y_pos = ball_x_pos, ball_y_pos
        for i in range(10):
            player_x_pos += ball_x_speed
            player_y_pos += ball_y_speed
            if player_y_pos > 768:
                player_y_pos += 768 - player_y_pos
                ball_y_speed *= -1
            if player_x_pos > 1366:
                player_x_pos += 1366 - player_x_pos
                ball_x_speed *= -1

        # We return that position
        return (player_x_pos, player_y_pos)
        '''
        return ball_x_pos, ball_y_pos

    def get_shortest_path(self, game):
        # This gets us the inputs to get to the target and the time needed to do so
        ai_pos_x = self.get_object_pos_x(game.base_entities[2])
        ai_pos_y = self.get_object_pos_y(game.base_entities[2])
        m = (ai_pos_y - self.target_y) / (ai_pos_x - self.target_x)
        time = ((((ai_pos_y - self.target_y) ** 2) + ((ai_pos_x - self.target_x) ** 2)) ** (1/2)) / self.max_speed
        return np.cos(np.arctan(m)), np.sin(np.arctan(m)), time

    # Fonction principale appelée par le loop:

    def ia_choice_lvl0(self, game):
        # Rappel: "game.base entities[0]" designe l'objet "Puck" 100% des cas.
        puck_pos_x = self.get_object_pos_x(game.base_entities[0])
        puck_pos_y = self.get_object_pos_y(game.base_entities[0])
        ai_pos_x = self.get_object_pos_x(game.base_entities[2])
        ai_pos_y = self.get_object_pos_y(game.base_entities[2])
        # puck_speed = self.get_puck_speed(game.base_entities[0])
        # opponent_speed = self.get_opponent_speed(game.players)

        if puck_pos_y < ai_pos_y:
            self.current_inputs[1] = -0.75

        if puck_pos_y > ai_pos_y:
            self.current_inputs[1] = 0.75

        if puck_pos_x < ai_pos_x:
            self.current_inputs[0] = -0.75

        if puck_pos_x > ai_pos_x:
            self.current_inputs[0] = 0.75

    def ia_choice_lvl1(self, game):
        # print(self.idea, self.current_inputs[0], self.current_inputs[1], self.target_x, self.target_y)


        # The prog should be fine, but there's a chance we just intercept instead of shooting

        # Rappel: "game.base entities[0]" designe l'objet "Puck" 100% des cas.
        puck_pos_x = self.get_object_pos_x(game.base_entities[0])
        puck_pos_y = self.get_object_pos_y(game.base_entities[0])
        ai_pos_x = self.get_object_pos_x(game.base_entities[2])
        ai_pos_y = self.get_object_pos_y(game.base_entities[2])
        # puck_speed = self.get_puck_speed(game.base_entities[0])
        # opponent_speed = self.get_opponent_speed(game.players)


        # I added the Idea, target_x and target_y attribute
        # If Idea = 0, we get new inputs
        # If not, we keep the inputs and tick down idea
        # target_x and target_y is where we are trying to go

        # Ok so here's the game plan :
        # If the puck is on the left of the screen, the pc will try to get it to the other side
        # If it's on the right, it will try to score
        if self.idea > 0:
            self.idea -= 1
        else:
            print(puck_pos_x, puck_pos_y, ai_pos_x, ai_pos_y)
            self.target_x, self.target_y = self.get_quickest_position(ai_pos_x, ai_pos_y, self.max_speed, puck_pos_x,
                                                                 puck_pos_y,
                                                                 game.base_entities[0].speed[0],
                                                                 game.base_entities[0].speed[1])
            # We have put a target on the position to hit the puck
            # line of coordinate y = mx + p
            print(self.idea, self.current_inputs[0], self.current_inputs[1], self.target_x, self.target_y)
            m_coeff = (ai_pos_y - self.target_y) / (ai_pos_x - self.target_x)
            p_coeff = (ai_pos_y - m_coeff * ai_pos_x)
            if puck_pos_x > 1366 / 2:
                # so if the puck is our zone

                if (768 / 4 > m_coeff * 1366 + p_coeff) or \
                        (768 * 3 / 4 < m_coeff * 1366 + p_coeff):
                    print("a")
                    # If the puck isn't aligned with the goal, we kick it
                    self.current_inputs[0], self.current_inputs[1], self.idea = self.get_shortest_path(game)
                else:
                    print("b")
                    # If it cannot, we gotta reposition
                    self.target_x = (ai_pos_x + 1366) / 2
                    self.target_y = (ai_pos_y + 768) / 2
                    self.current_inputs[0], self.current_inputs[1], self.idea = self.get_shortest_path(game)
            else:
                # If we can score, we go for it
                # If not, we reposition
                if (768 / 4 < p_coeff) and (768 * 3 / 4 > p_coeff):
                    print("c")
                    # If we can score, full throttle
                    self.current_inputs[0], self.current_inputs[1], self.idea = self.get_shortest_path(game)
                else:
                    print("d")
                    # We go at the center to await our shot
                    self.target_x = 1366/2
                    self.target_y = 768/2
                    self.current_inputs[0], self.current_inputs[1], self.idea = self.get_shortest_path(game)