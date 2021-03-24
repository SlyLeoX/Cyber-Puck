import pygame
import sys

from classOneGame import Movable
from ClassEffect import effectType
from classMovableControlsAux import controls_mapping


class PlayerType(Movable):

    def __init__(self, x, y, charinfo, keys, texture="bumper.gif"):

        Movable.__init__(self, x, y, charinfo, keys, texture="bumper.gif")

        self.score = 0

        self.current_inputs = [0, 0]
        self.map = controls_mapping(keys)
        self.number = -1

        self.max_stamina = charinfo[1]
        self.max_special = 12

        self.current_stamina = self.max_stamina
        self.current_special = 0

        self.active_pow = []

        self.icon = charinfo[2]


    def get_inputs(self, events):

        # events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYUP and 0:

                if pygame.key.get_pressed()[self.map["up"]] == False and pygame.key.get_pressed()[
                    self.map["down"]] == False:
                    self.speed[1] = 0
                if pygame.key.get_pressed()[self.map["left"]] == False and pygame.key.get_pressed()[
                    self.map["right"]] == False:
                    self.speed[0] = 0

            if event.type == pygame.KEYDOWN:
                # The 0.5 down there could be later replaced by the acceleration stats.
                # The 3 down there could be later replaced by the strength stats.
                if event.key == self.map["up"]:
                    if self.speed[1] > -3: self.speed[1] -= 0.4
                    if self.speed[1] > 0: self.speed[1] = 0
                elif event.key == self.map["down"]:
                    if self.speed[1] < 0: self.speed[1] = 0
                    if self.speed[1] < 3: self.speed[1] += 0.4

                if event.key == self.map["left"]:
                    if self.speed[0] > 0: self.speed[0] = 0
                    if self.speed[0] > -3: self.speed[0] -= 0.4
                elif event.key == self.map["right"]:
                    if self.speed[0] < 0: self.speed[0] = 0
                    if self.speed[0] < 3: self.speed[0] += 0.4


            if event.type == pygame.JOYAXISMOTION and event.instance_id == self.number - 1:
                if event.axis == 0:
                    self.speed[0] = event.value
                if event.axis == 1:
                    self.speed[1] = event.value

    def get_inputs_2(self, events, game):

        for event in events:

            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYUP:

                if event.key == self.map["up"] and self.current_inputs[1]==-1:
                    self.current_inputs[1] = 0
                elif event.key == self.map["down"] and self.current_inputs[1]==1:
                    self.current_inputs[1] = 0

                if event.key == self.map["left"] and self.current_inputs[0]==-1:
                    self.current_inputs[0] = 0
                elif event.key == self.map["right"] and self.current_inputs[0]==1:
                    self.current_inputs[0] = 0

            if event.type == pygame.KEYDOWN:

                if event.key == self.map["up"]:
                    self.current_inputs[1] = -1
                elif event.key == self.map["down"]:
                    self.current_inputs[1] = 1

                if event.key == self.map["left"]:
                    self.current_inputs[0] = -1
                elif event.key == self.map["right"]:
                    self.current_inputs[0] = 1

                if event.key == self.map["spe_move"]:
                    self.dash(game)

                if event.key == self.map["ultra"]:
                    self.ultra(game)

    def apply_inputs(self):

        #Instant direction change code
        for i in range(2):
            if self.current_inputs[i] == 1 and self.speed[i] < 0:
                self.speed[i]=0
            if self.current_inputs[i] == -1 and self.speed[i] > 0:
                self.speed[i]=0
        #To replace with char stats
        acc = 0.1
        max = 10

        #print(self.current_inputs)

        for i in range(2):
            self.speed[i] += acc*self.current_inputs[i] if abs(self.speed[i]) < max else 0

    def dash(self,game):
        if self.current_stamina >= 5:
            self.current_stamina -= 5
            print("DASH! remaining:",self.current_stamina)
            for i in range(32):
                self.run()
                self.boundary_check((game.width, game.height))
                self.physics_check(game.base_entities)
        else:
            print("Dash failed")

    def ultra(self,game):

        if self.current_special == 12:
            print("ULTRA")
            self.current_special -= 12
            self.active_pow.append(effectType(self,20*5*60,"ultra0"))
        else:
            print("ULTRA FAIL!")


