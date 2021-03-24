import pygame

from classMovable import Movable
from classPlayer import PlayerType
from classCom import ComType
from classImmuable import goalType
from ClassEffect import effectType

#Placeholder while we don't have proper file transmission between parts...
player_pos=[[1/6, 2],[5/6, 1/2]]


class partyOn:

    def __init__(self, system_parameters, player_parameters,terrain):

        self.screen = system_parameters[0]
        self.width = system_parameters[1][0]
        self.height = system_parameters[1][1]

        self.base_entities = []
        self.base_entities.append(Movable(self.width/2, self.height/2, [5], "0", "intro_ball.gif"))
        for i in range(2):
            pos = player_pos[i]
            par = player_parameters[i]
            if par[0][:-1] == "PLAYER" or 1: #ALWAYS ON FOR NOW
                self.base_entities.append(PlayerType(pos[0]*self.width, pos[1]*self.height, par[1], par[2]))
            else:
                self.base_entities.append(ComType)

        self.players = self.base_entities[1:]

        self.zone_parts = []
        self.zone_parts.append(goalType(64*self.width/1920, (self.height * 0.5) - 75))
        self.zone_parts.append(goalType(self.width - (64+24)*self.width/1920, (self.height * 0.5) - 75))

        self.bg = pygame.image.load(terrain[0]).convert()
        self.bg = pygame.transform.scale(self.bg, system_parameters[1])
        self.terrain_resistance = terrain[1]

    def apply_all_effects(self):
        for player in self.players:
            if player.active_pow!=[]: print(player.active_pow,player.active_pow[0].types,player.active_pow[0].lenght)
            for capacity in player.active_pow:
                print("He went there! Capacity's time:", pygame.time.get_ticks()-capacity.origin)
                capacity.effects_apply(player, (self.width,self.height,self.screen))

                if capacity.last_frame() == True:
                    print("Lastframe!")
                    player.active_pow.remove(capacity)


    def complete_frame(self):
        for entity in self.base_entities:
            entity.boundary_check((self.width, self.height, self.screen))
            entity.physics_check(self.base_entities)
            entity.run()

    def get_allinputs(self):
        events = pygame.event.get()
        for player in self.players:
            player.get_inputs_2(events,self)
            player.apply_inputs()

    def goal_verif(self):
        for i in range(2):
            if self.zone_parts[i].rect.colliderect(self.base_entities[0].rect):
                print("GOAL!")
                self.players[i].score += 1
                return 0
        return 1

    def goal_verif2(self):

        cy = self.base_entities[0].rect.centery
        arg = (cy > self.zone_parts[0].rect.centery and cy < self.zone_parts[0].rect2.centery)

        if self.base_entities[0].rect.left < (64+5)*self.width/1920 and arg:
            self.players[1].score += 1
            return 0
        elif self.base_entities[0].rect.right > self.width-(64+5)*self.width/1920 and arg:
            self.players[0].score += 1
            return 0

        return 1

    def blit_entities(self):
        for entity in self.base_entities:
            self.screen.blit(entity.tex, entity.rect)

    def blit_stadium(self):
        for zone in self.zone_parts:
            for pole in zone.rectlist:
                self.screen.blit(zone.tex, pole)

    def blit_scores(self):
        black = 0, 0, 0
        blue = 65, 65, 255
        red = 255, 65, 65
        misc_text = pygame.font.SysFont('Calibri', 92)
        score1 = misc_text.render(str(self.players[0].score), False, blue)
        score2 = misc_text.render(str(self.players[1].score), False, red)
        self.screen.blit(score1, (50, self.height-110))
        self.screen.blit(score2, (self.width - 95, self.height-110))

    def blit_playtags(self):
        red = 255, 65, 65
        blue = 65, 65, 255
        misc_text = pygame.font.SysFont('Calibri', 30)
        playtag1 = misc_text.render("P1", False, blue)
        playtag2 = misc_text.render("P2", False, red)
        self.screen.blit(playtag1, (self.players[0].rect.x - 15, self.players[0].rect.y - 15))
        self.screen.blit(playtag2, (self.players[1].rect.x - 15, self.players[1].rect.y - 15))

    def blit_bg(self):
        self.screen.blit(self.bg, (0, 0))

    def blit_overlay(self):
        overlay = pygame.image.load("Cyberpeck_Overlay_III_mk1.gif").convert_alpha()
        overlay = pygame.transform.scale(overlay, (self.width, self.height))

        self.screen.blit(overlay, (0,0))

    def entities_reset(self):
        for entity in self.base_entities:
            entity.speed = [0, 0]
        self.players[0].true_pos[0] = self.players[0].rect.x = self.width * 1 / 6
        self.players[1].true_pos[0] = self.players[1].rect.x = self.width * 5 / 6
        self.players[0].true_pos[1] = self.players[0].rect.y = self.height / 2
        self.players[1].true_pos[1] = self.players[1].rect.y = self.height / 2

        self.base_entities[0].true_pos[0]=self.players[0].rect.x = self.width / 2
        self.base_entities[0].true_pos[1] = self.players[0].rect.y = self.height / 2

    def stamina_restitution(self):
        if pygame.time.get_ticks()%3 == 0:
            for player in self.players:
                if player.current_stamina < player.max_stamina:
                    player.current_stamina += 0.1

    def blit_stamina(self):

        green = 0, 255, 0

        for player in self.players:
            bar_width = (player.current_stamina/player.max_stamina) * (700*self.width/1920)

            if player.base_x < (self.width/2) : x_pos = 184*self.width/1920
            else: x_pos = self.width - (185 *self.width/1920) - bar_width

            rect = ((x_pos,15*self.height/1080),(bar_width,40*self.height/1080))

            pygame.draw.rect(self.screen, green, rect)

    def blit_special(self):

        yellow = 255, 255, 0

        for player in self.players:
            bar_width = (player.current_special/player.max_special) * (700*self.width/1920)

            if player.base_x < (self.width/2) : x_pos = 185*self.width/1920
            else: x_pos = self.width - (185 *self.width/1920) - bar_width

            rect = ((x_pos,66*self.height/1080),(bar_width,40*self.height/1080))

            pygame.draw.rect(self.screen, yellow, rect)

    def blit_timer(self,sec):

        white = 255, 255, 255

        misc_text = pygame.font.SysFont('Calibri', 30)
        timer = misc_text.render((str(sec//60) + ":" + str((sec//10) % 6) + str(sec%10)), False, white)

        self.screen.blit(timer, (self.width/2 - 25, 33 * self.height/1080))

    def blit_char_icon(self):

        for player in self.players:
            icon = (player.icon[:-4]) + "_mini.gif"

            icon = pygame.image.load(icon).convert_alpha()
            icon = pygame.transform.scale(icon, (round(160*self.width/1920), round(160*self.height/1080)))



            if player.base_x < (self.width/2) : self.screen.blit(icon, (17*self.width/1920, 17*self.height/1080))
            else: self.screen.blit(icon, (self.width-(17+158)*self.width/1920, 17*self.height/1080))




