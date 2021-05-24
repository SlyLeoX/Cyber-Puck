import pygame
import sys

from CORE.classOneGame import Movable
from CORE.classEffect import EffectType
from CORE.auxiliary_Controls import controls_mapping
from CORE.auxiliary_Stats import return_charstats


class PlayerType(Movable):

    def __init__(self, x, y, infopack, number=-1):

        Movable.__init__(self, x, y, infopack)

        # TODO: Change the following static string by a call ajusting the texture to the character.
        # Load and resize the image of the player pawn.
        self.tex = pygame.image.load(r"CORE\ressources\misc\palet_alt.png").convert_alpha()
        self.tex = pygame.transform.scale(self.tex, (55, 55))
        self.rect = self.tex.get_rect()

        self.score = 0
        self.number = number
        self.charname = infopack[1]

        # Current_inputs stocks the current asked movement direction by the player (ex: [1,1]=DownRight)
        self.current_inputs = [0, 0]
        # Map stocks the avaiable input keys of the player.
        self.map = controls_mapping(infopack[2])

        # TODO: Make Acceleration and Max_speed among the charachters'stats.
        self.acceleration = 0.3
        self.max_speed = 8

        self.max_stamina = return_charstats(infopack[1])[1]
        self.max_special = return_charstats(infopack[1])[2]

        # Initialization of energy and super-technique gauges: energy stats at max and technique starts empty.
        self.current_stamina = self.max_stamina
        self.current_special = 0

        # Will contain the player's current active special techniques.
        self.active_pow = []

        # Stores the chosen character's portrait.
        self.icon = return_charstats(infopack[1])[3]

        # The following store the characteristics of the character's special techniques
        # The dash is common to every character
        # effects pattern=[number of frames of effect (theoretical),("type0,effect1,effect2,...")]
        self.ultras = return_charstats(infopack[1])[5]
        self.supers = return_charstats(infopack[1])[4]
        # self.passives = return_charstats(infopack[1])[6]
        self.dashs = [10*60, "dash0,self_speedup4"]

        self.inputs = {}

        # elements to add :
        # player.map_axis would be dictionary of type player.map_axis[axis number] = "action"
        # player.input would be a dictionary of type player.input["action"] = "pressing" or "pressed" or "released"
        # player.input_axis would be a dictionary of type player.input[axis_number] = value

    # Verify for each player if a key belonging to their "map" is pressed, and therefore registering this inputs.
    # If the input launches a special technique: the corresponding function is called to ignite that technique.
    def get_inputs_2(self, events, game):

        for event in events:

            if event.type == pygame.QUIT: sys.exit()

            # The following resets stored "currently asked direction" when a key is released.
            if event.type == pygame.KEYUP:

                if event.key == self.map["up"] and self.current_inputs[1] == -1:
                    self.current_inputs[1] = 0
                elif event.key == self.map["down"] and self.current_inputs[1] == 1:
                    self.current_inputs[1] = 0

                if event.key == self.map["left"] and self.current_inputs[0] == -1:
                    self.current_inputs[0] = 0
                elif event.key == self.map["right"] and self.current_inputs[0] == 1:
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
                if event.key == self.map["sup_move"]:
                    self.super(game)
                if event.key == self.map["ultra"]:
                    self.ultra(game)

            # Joysticks management: movements.
            if event.type == pygame.JOYAXISMOTION and event.instance_id == self.number:
                if event.axis == 0:
                    self.current_inputs[0] = event.value
                if event.axis == 1:
                    self.current_inputs[1] = event.value
            # Joystick management: techniques.
            if event.type == pygame.JOYBUTTONDOWN and event.instance_id == self.number:
                print(event.button)
                if event.button in self.map.values():
                    self.inputs[event.button] = "pressing"
                if event.button == self.map["spe_move2"]:
                    self.dash(game)
                if event.button == self.map["sup_move2"]:
                    self.super(game)
                if event.button == self.map["ultra2"]:
                    self.ultra(game)

            if event.type == pygame.JOYBUTTONUP and event.instance_id == self.number:
                if event.button in self.map.values():
                    self.inputs[event.button] = "releasing"

    # Increase/Decrease speeds of the players according to "current_inputs"
    def apply_inputs(self):

        # The following is a gameplay choice allowing to instantly change direction without having a deceleration phase.
        for i in range(2):
            if self.current_inputs[i] == 1 and self.speed[i] < 0:
                self.speed[i] = 0
            if self.current_inputs[i] == -1 and self.speed[i] > 0:
                self.speed[i] = 0

        # To replace with char stats
        acc = self.acceleration
        max = self.max_speed

        for i in range(2):
            self.speed[i] += acc*self.current_inputs[i] if abs(self.speed[i]) < max else 0

    # The dash isn't a proper Effect Type, i only make the player advance 32 times in 1 frame to simulate the speedup.
    def dash(self, game):
        #   Checks if the player has enough energy. If so remove the required energy and launch the dash.
        if self.current_stamina >= 5:
            self.current_stamina -= 5
            print("DASH! remaining:", self.current_stamina)
            for i in range(32):
                self.run()
                self.boundary_check((game.width, game.height))
                self.physics_check(game.base_entities)
        else:
            print("Dash failed")

    # Create the effect type if the player has enough "technique points" according to stats linked to the character.
    def super(self, game):
        if self.current_special >= 6:
            print("SUPER")
            self.current_special -= 6
            self.active_pow.append(EffectType(self, self.supers[0], self.supers[1], game))
        else:
            print("SUPER FAIL!")

    # Create the effect type if the player has enough "technique points" according to stats linked to the character.
    def ultra(self, game):
        if self.current_special >= 12:
            print("ULTRA")
            self.current_special -= 12
            self.active_pow.append(EffectType(self, self.ultras[0], self.ultras[1], game))
        else:
            print("ULTRA FAIL!")


