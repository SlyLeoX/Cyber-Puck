import pygame

from classMovable import Movable
from classPlayer import PlayerType
from classCom import ComType
from classImmuable import zoneType


system_parameters=[1366,768]
player_parameters=[["PLAYER1","keyboard1","bumper.gif"],["COM","COM1","bumper.gif"]]
#Placeholder while we don't have proper file transmission between parts...
player_pos=[[1/6, 2, 10, "keyboard1"],[5/6, 1/2, 10, "keyboard2"]]
terrain=[]

class partyOn:

    def __init__(self,system_parameters,player_parameters):

        self.screen = system_parameters[0]
        self.width = system_parameters[1]
        self.height = system_parameters[2]

        self.base_entities = []
        self.base_entities.append(Movable(self.width/2, self.height/2, 5, "0", "intro_ball.gif"))
        for i in range(2):
            p=player_pos[i]
            if player_parameters[i][0][:-1] == "PLAYER" or 1:
                self.base_entities.append(PlayerType(p[0]*self.width, p[1]*self.height, p[2], p[3]))
            else:
                self.base_entities.append(ComType)
        self.players=self.base_entities[1:]

        self.zone_parts = []
        self.zone_parts.append(zoneType(0, (self.height * 0.5) - 100))
        self.zone_parts.append(zoneType(self.width - 20, (self.height * 0.5) - 100))

        self.scores = []

    def complete_frame(self):
        for entity in self.base_entities:
            entity.boundary_check((self.width, self.height))
            entity.physics_check(self.base_entities)
            entity.run()

    def get_allinputs(self):
        events = pygame.event.get()
        for player in self.players:
            player.get_inputs_2(events)
            player.apply_inputs()

    def goal_verif(self):
        for i in range(2):
            if self.zone_parts[i].rect.colliderect(self.base_entities[0].rect):
                print("GOAL!")
                self.players[i].score += 1
                return(0)
        return (1)

    def blit_entities(self):
        for entity in self.base_entities:
            self.screen.blit(entity.tex, entity.rect)

    def blit_stadium(self):
        for zone in self.zone_parts:
            self.screen.blit(zone.tex, zone.rect)

    def blit_scores(self):
        black = 0,0,0
        misc_text = pygame.font.SysFont('Calibri', 30)
        score1 = misc_text.render("Player 1 : " + str(self.players[1].score), False, black)
        score2 = misc_text.render("Player 2 : " + str(self.players[0].score), False, black)
        self.screen.blit(score1, (20, 0))
        self.screen.blit(score2, (self.width - 200, 0))

    def blit_playtags(self):
        red = 255, 65, 65
        blue = 65, 65, 255
        misc_text = pygame.font.SysFont('Calibri', 30)
        playtag1 = misc_text.render("P1", False, blue)
        playtag2 = misc_text.render("P2", False, red)
        self.screen.blit(playtag1, (self.players[0].rect.x - 15, self.players[0].rect.y - 15))
        self.screen.blit(playtag2, (self.players[1].rect.x - 15, self.players[1].rect.y - 15))

    def entities_reset(self):
        for entity in self.base_entities:
            entity.speed=[0,0]
        self.players[0].true_pos[0]=self.players[0].rect.x = self.width * 1 / 6
        self.players[1].true_pos[0] = self.players[1].rect.x = self.width * 5 / 6
        self.players[0].true_pos[1] = self.players[0].rect.y = self.height / 2
        self.players[1].true_pos[1] = self.players[1].rect.y = self.height / 2

        self.base_entities[0].true_pos[0]=self.players[0].rect.x = self.width / 2
        self.base_entities[0].true_pos[1] = self.players[0].rect.y = self.height / 2





