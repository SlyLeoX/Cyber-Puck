import pygame

from CORE.classMovable import Movable
from CORE.classPlayer import PlayerType
from CORE.classCom import AiType
from CORE.classImmuable import goalType
from CORE.classEffect import EffectType

from CORE.auxiliary_Stats import return_stadiumstats
from CORE.auxiliary_Toolbox import text_box, text_screen

# Reference to know where are the players supposed to start
player_pos = [[1/6, 1/2], [5/6, 1/2]]


class PartyOn:

    # Some function of the class have been put in the following files to unload the classOneGame.py .
    # The technique allow to use these functions the same as usual, except you have to manually put the 'self' argument.

    from CORE.auxiliary_FX import side_sounds, side_animations, collide_sounds, collide_animations

    def __init__(self, system_parameters, player_parameters, terrain):

        # Extracting useful screen parameters for easy use later.
        self.screen = system_parameters[0]
        self.width = system_parameters[1][0]
        self.height = system_parameters[1][1]

        # Adding the Puck to the list of active entities in game.
        infopack = ["PUCK1", "0", "0"]
        self.base_entities = []
        self.base_entities.append(Movable(self.width/2, self.height/2, infopack))

        for i in range(2):
            # Extracting parameters for the 2 player from the arguments.
            pos = player_pos[i]
            infopack = player_parameters[i]
            # The condition allow to determine if the actor initializing is a human or a IA
            # The player is then Added to the list of active entities in game.
            # Note: AiType inherits PlayerType, PlayerType inherits Movable.
            # The arguments to create these is [x_position,y_position,set of misc. info,id 'i' used for identification]
            if infopack[0][:-1] == "PLAYER":
                self.base_entities.append(PlayerType(pos[0]*self.width, pos[1]*self.height, infopack, i))
            else:
                self.base_entities.append(AiType(pos[0]*self.width, pos[1]*self.height, infopack, i))

        # Create an array containing only the players' reference for easier use.
        self.players = self.base_entities[1:]

        # Creating the thwo goals on each side of the terrain with proper coordiantes.
        self.zone_parts = []
        self.zone_parts.append(goalType(64*self.width/1920, (self.height * 0.5) - 75))
        self.zone_parts.append(goalType(self.width - (64+24)*self.width/1920, (self.height * 0.5) - 75))

        # Loading the background image and extracting the ""friction"" parameter used for speed reduction.
        self.bg = pygame.image.load(return_stadiumstats(terrain)[0]).convert()
        self.bg = pygame.transform.scale(self.bg, system_parameters[1])
        self.terrain_resistance = return_stadiumstats(terrain)[1]

        # Loading the interface overlay image.
        self.overlay = pygame.image.load(r"CORE\ressources\ui\Cyberpeck_Overlay_III_mk1.gif").convert_alpha()
        self.overlay = pygame.transform.scale(self.overlay, (self.width, self.height))

        # Load the miniature character portraits, adjusting their size and making the right character face the center.
        self.char_icons = []
        for player in self.players:
            icon = (player.icon[:-4]) + "_mini.png"
            icon = pygame.image.load(icon).convert_alpha()
            icon = pygame.transform.scale(icon, (round(160 * self.width / 1920), round(160 * self.height / 1080)))
            self.char_icons.append(icon)
        self.char_icons[1] = pygame.transform.flip(self.char_icons[1], True, False)

        # Load the image effect for collision with the border.
        self.sideimpact_effect = pygame.image.load(r"CORE\ressources\vfx\side_impact.gif").convert_alpha()
        self.sideimpact_effect = pygame.transform.scale(self.sideimpact_effect, (86, 39))

        # Load the image effect for collision with other actors.
        self.centerimpact_effect = pygame.image.load(r"CORE\ressources\vfx\center_impact.gif").convert_alpha()
        self.centerimpact_effect = pygame.transform.scale(self.centerimpact_effect, (94, 94))

    # Checks if both players have effects to get applied or to get removed.
    def apply_all_effects(self):
        for player in self.players:
            for capacity in player.active_pow:
                capacity.effects_apply(player, (self.width, self.height, self.screen), self.base_entities)

                if capacity.last_frame():
                    player.active_pow.remove(capacity)
                    del capacity

    # Calls the functions for borders checking, physics and movement of the actors, and visual effects if needed.
    def complete_frame(self):
        for entity in self.base_entities:
            # Ignore your IDE if it asks for more arguments in the following calls.
            i = entity.boundary_check((self.width, self.height))
            if i: self.side_animations(entity, i)
            i = entity.physics_check(self.base_entities)
            if i: self.collide_animations(i)
            entity.run()

    # Checks if a player is an Ia, if so, calls the function liked to its level.
    def ia_turn(self, game):
        for player in self.players:

            if type(player) == AiType:
                if player.level == 0:
                    player.ia_choice_lvl0(game)
                if player.level == 1:
                    player.ia_choice_lvl1(game)
                if player.level == 2:
                    # To be completed if the IA management of effects is made.
                    pass

    # Checks for input made during the frame. Apply the inputs made by each human player for themselves.
    # Also check if some particular keys have been pushed: F8 (debug info), F9 (hard stop) and ESC (Pause).
    def get_allinputs(self):
        events = pygame.event.get()
        for player in self.players:
            player.get_inputs_2(events, self)
            player.apply_inputs()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F8:
                    print("Debug information requested")
                    self.debug_informations()
                    return 1
                if event.key == pygame.K_F9:
                    print("STOP!!")
                    return 0
                if event.key == pygame.K_ESCAPE:
                    print("PAUSE!!")
                    return -1
        return 1

    # Print a pause screen if called then tracks for new push on escape key to end the pause.
    def pause_screen(self):
        press = 0
        while press == 0:

            # For text_box code consult "auxiliary_toolbox.py"
            text_box((self.screen, (self.width, self.height)), "PAUSE", "red", 250)

            # After having shown the PAUSE sign for a quarter of a second, check if the 'echap' key has been pressed.
            events = pygame.event.get()
            for searching in events:
                if searching.type == pygame.KEYDOWN:
                    if searching.key == pygame.K_ESCAPE:
                        press = 1

    # Tracks if the coordinates of the puck are in a player's goal, if so add a points to the good player and send 0.
    def goal_verif2(self):

        cy = self.base_entities[0].rect.centery
        arg = (self.zone_parts[0].rect.centery < cy < self.zone_parts[0].rect2.centery)

        if self.base_entities[0].rect.left < (64+5)*self.width/1920 and arg:
            self.players[1].score += 1
            return 0
        elif self.base_entities[0].rect.right > self.width-(64+5)*self.width/1920 and arg:
            self.players[0].score += 1
            return 0

        return 1

    # Prints the entities (pucks and players) at the right place on screen
    def blit_entities(self):
        for entity in self.base_entities:
            self.screen.blit(entity.tex, entity.rect)

    # Prints the goals' "poles" at the right place on screen
    def blit_stadium(self):
        for zone in self.zone_parts:
            for pole in zone.rectlist:
                self.screen.blit(zone.tex, pole)

    # Print the players' scores on the bottom of the screen with a color.
    def blit_scores(self):
        blue = 65, 65, 255
        red = 255, 65, 65
        misc_text = pygame.font.SysFont('Calibri', 92)
        score1 = misc_text.render(str(self.players[0].score), False, blue)
        score2 = misc_text.render(str(self.players[1].score), False, red)
        self.screen.blit(score1, (50, self.height-110))
        self.screen.blit(score2, (self.width - 95, self.height-110))

    # Print the players' ID next to their pawn the same color as their score.
    def blit_playtags(self):
        red = 255, 65, 65
        blue = 65, 65, 255
        misc_text = pygame.font.SysFont('Calibri', 30)
        playtag1 = misc_text.render("P1", False, blue)
        playtag2 = misc_text.render("P2", False, red)
        self.screen.blit(playtag1, (self.players[0].rect.x - 15, self.players[0].rect.y - 15))
        self.screen.blit(playtag2, (self.players[1].rect.x - 15, self.players[1].rect.y - 15))

    # Print the background image.
    def blit_bg(self):
        self.screen.blit(self.bg, (0, 0))

    # Print the overlay image.
    def blit_overlay(self):
        self.screen.blit(self.overlay, (0,0))

    # Give back a little amount of energy to every player every 3 frames.
    def stamina_restitution(self):
        if pygame.time.get_ticks() % 3 == 0:
            for player in self.players:
                if player.current_stamina < player.max_stamina:
                    player.current_stamina += 0.1

    # Print the energy bar for every player at the right place on the overlay.
    def blit_stamina(self):

        green = 0, 255, 0

        for player in self.players:
            bar_width = (player.current_stamina/player.max_stamina) * (700*self.width/1920)

            if player.base_x < (self.width/2): x_pos = 184*self.width/1920
            else: x_pos = self.width - (185 * self.width/1920) - bar_width

            rect = ((x_pos, 15*self.height/1080), (bar_width, 40*self.height/1080))

            pygame.draw.rect(self.screen, green, rect)

    # Print the "special techniques" bar for every player at the right place on the overlay.
    def blit_special(self):

        yellow = 255, 255, 0

        for player in self.players:
            bar_width = (player.current_special/player.max_special) * (700*self.width/1920)

            if player.base_x < (self.width/2): x_pos = 185*self.width/1920
            else: x_pos = self.width - (185 * self.width/1920) - bar_width

            rect = ((x_pos, 66*self.height/1080), (bar_width, 40*self.height/1080))

            pygame.draw.rect(self.screen, yellow, rect)

    # Print the chronometers' count at the right place on the overlay.
    def blit_timer(self, sec):

        white = 255, 255, 255

        misc_text = pygame.font.SysFont('Calibri', 30)
        timer = misc_text.render((str(sec//60) + ":" + str((sec//10) % 6) + str(sec % 10)), False, white)

        self.screen.blit(timer, (self.width/2 - 25, 33 * self.height/1080))

    # Print the characters' reduced portraits for every player at the right place on the overlay.
    def blit_char_icon(self):

        for i in range (2):
            player = self.players[i]
            if player.base_x < (self.width/2): self.screen.blit(self.char_icons[i], (16*self.width/1920, 12*self.height / 1080))
            else: self.screen.blit(self.char_icons[i], (self.width-(16+158)*self.width/1920, 12*self.height/1080))

    # Print the "match's objectives" a the start of the match, so the conditions to win: parameter and asked value.
    def begin_screen(self, parameter, objective):
        self.screen.fill((0, 0, 0))
        print("THAT IS:",parameter)
        if parameter == "score":
            text = "BE THE FIRST TO SCORE "+str(objective)+" POINTS"
        else:
            text = "HAVE THE HIGHEST SCORE IN "+str(objective)+" SECONDS"
        text_screen((self.screen, (self.width, self.height)), text, "black", 5000, 40)

    # Print the winner's character name at the end of the match, also returns a value depending of the winner.
    def end_screen(self):

        if self.players[0].score > self.players[1].score:
            winner = 0
        elif self.players[1].score > self.players[0].score:
            winner = 1
        else:
            winner = -1

        if winner < 0:
            text_box((self.screen, (self.width, self.height)), "PAR", "blue", 5000)
        else:
            text_box((self.screen, (self.width, self.height)), self.players[winner].charname+" WINS", "green", 5000)

        return winner

    # Reset every entities' speed, active effects and position on the terrain.
    # Also if the checked player is an Ia, resets its current "mode" (ex: attack/defense/...)
    def entities_reset(self):
        for entity in self.base_entities:
            entity.speed = [0, 0]
            entity.speed_multiplier = [1, 1]
            entity.tangible = True

        for player in self.players:
            if type(player) == "AiType":
                player.idea = 0

            for effect in player.active_pow:
                del effect
            player.active_pow = []

        self.players[0].true_pos[0] = self.players[0].rect.x = self.width * 1 / 6
        self.players[1].true_pos[0] = self.players[1].rect.x = self.width * 5 / 6
        self.players[0].true_pos[1] = self.players[0].rect.y = self.height / 2
        self.players[1].true_pos[1] = self.players[1].rect.y = self.height / 2

        self.base_entities[0].true_pos[0] = self.players[0].rect.x = self.width / 2
        self.base_entities[0].true_pos[1] = self.players[0].rect.y = self.height / 2

    # Should be removed, prints some values upon pressing F8 in the console only.
    def debug_informations(self):

        for i in range(2):
            print("Player NO.", i)
            print("Multipliers:", self.players[i].speed_multiplier)