#Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)

import pygame
import sys
import random as rd
import numpy as np

from time import sleep

from Prototyp_Parameters import controls_mapping

white = 255, 255, 255
black = 0, 0, 0
red = 255, 65, 65
blue = 65, 65, 255

if __name__ == '__main__':

    loop = 1
    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    class Movable:

        def __init__(self, x, y, mass, keys, texture="bumper.gif"):
            self.tex = pygame.image.load(texture).convert()
            self.rect = self.tex.get_rect()

            self.speed = [0, 0]
            self.true_pos = [x, y]
            self.true_center = [x - (self.rect.size[0])/2 , y - (self.rect.size[1])/2]
            self.ray = self.rect.size[0]/2

            self.rect.x = x
            self.rect.y = y

            self.mass = mass
            self.map = controls_mapping(keys)

            self.last_impact = 0

            self.number = -1

        def get_truecenter(self):

            self.true_center = [self.rect.x - (self.rect.size[0]) / 2, self.rect.y - (self.rect.size[1]) / 2]

        def run(self, resistance=5000):

            #if rd.randint(0, resistance) == resistance:
                #print("Slow down!")

            for i in range(0,2):
                if self.speed[i] > 0: self.speed[i] -= 1/resistance
                elif self.speed[i] < 0: self.speed[i] += 1/resistance

            # rect = {1: self.rect.x, 2: self.rect.y}
            for i in range(0, 2):
                self.true_pos[i] += self.speed[i]
                # if self.true_pos != [0, 0]: print(self.true_pos)
                # rect[i] = self.true_pos[i]

            self.rect.x = self.true_pos[0]
            self.rect.y = self.true_pos[1]

            self.get_truecenter()

            # self.rect = self.rect.move(self.speed[0], self.speed[1])

        def boundary_check(self):
            # print("Check before moving.")
            w = 0

            if self.true_center[0] < -25:
                self.rect.x = 0
                self.speed[0] *= -1
                w = 1

            if self.true_center[0] > (width-75):
                self.rect.x = width-50
                self.speed[0] *= -1
                w = 1

            if self.true_center[1] < -25:
                self.rect.y = 0
                self.speed[1] *= -1
                w = 1

            if self.true_center[1] > (height-75):
                self.rect.y = height-50
                self.speed[1] *= -1
                w = 1

            if w: self.last_impact = pygame.time.get_ticks()

        def physics_check(self, sentities):
            # print("Check before moving")
            for lentity in sentities:
                #if self.rect.colliderect(lentity.rect) and (pygame.time.get_ticks()-self.last_impact > 16 or pygame.time.get_ticks()-lentity.last_impact > 16 ):
                if (self.true_center[0] - lentity.true_center[0])**2 + (self.true_center[1] - lentity.true_center[1])**2 < (self.ray + lentity.ray)**2 and (
                        pygame.time.get_ticks() - self.last_impact > 16 or pygame.time.get_ticks() - lentity.last_impact > 16):

                    if abs(self.speed[0])+abs(self.speed[1])>abs(lentity.speed[0])+abs(lentity.speed[1]):
                        a = self
                        b = lentity
                    else:
                        a = lentity
                        b = self

                    #a, b = self, lentity

                    self.last_impact = pygame.time.get_ticks()
                    lentity.last_impact = pygame.time.get_ticks()

                    relative_v = [a.speed[0]-b.speed[0], a.speed[1]-b.speed[1]]

                    if a.true_center[0] == b.true_center[0]:  # temporary patch (Romeo  knows da way ! )

                            b.speed[1] = a.speed * round(b.mass / a.mass )

                    else: #Proper physics calculated.

                        c = (a.true_center[1] - b.true_center[1])/(a.true_center[0] - b.true_center[0])
                        s = (relative_v[0])*(np.cos(np.tan(c)))+(relative_v[1])*(np.sin(np.tan(c)))

                        va = s - ((2*s*b.mass)/(a.mass + b.mass))
                        vb = ((2*s*a.mass)/(a.mass + b.mass))

                        a.speed[0] = va * (np.cos(np.tan(c)))
                        a.speed[1] = va * (np.sin(np.tan(c)))

                        b.speed[0] = vb * (np.cos(np.tan(c)))
                        b.speed[1] = vb * (np.sin(np.tan(c)))

                    print(self.speed, lentity.speed)

                    while (self.true_center[0] - lentity.true_center[0])**2 + (self.true_center[1] - lentity.true_center[1])**2 < (self.ray + lentity.ray)**2:
                        b.run()
                        b.boundary_check()

                        # print("IMPACT", self, lentity, lentity.dspeed[0], lentity.dspeed[1])
                        #self.speed[1], lentity.speed[1] = lentity.speed[1], self.speed[1]
                        #self.speed[0], lentity.speed[0] = lentity.speed[0], self.speed[0]
                        #self.rect = self.rect.move(self.speed)

                    return 1
            return 0


    class PlayerType(Movable):

        def get_inputs(self, events):

            # events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYUP and 0:

                    if pygame.key.get_pressed()[self.map["up"]] == False and pygame.key.get_pressed()[self.map["down"]] == False:
                        self.speed[1] = 0
                    if pygame.key.get_pressed()[self.map["left"]] == False and pygame.key.get_pressed()[self.map["right"]] == False:
                        self.speed[0] = 0

                if event.type == pygame.KEYDOWN:
                    # The 0.5 down there could be later replaced by the acceleration stats.
                    # The 3 down there could be later replaced by the strength stats.
                    if event.key == self.map["up"]:
                        if self.speed[1] > -3: self.speed[1] -= 0.5
                        if self.speed[1] > 0: self.speed[1] = 0
                    elif event.key == self.map["down"]:
                        if self.speed[1] < 0: self.speed[1] = 0
                        if self.speed[1] < 3: self.speed[1] += 0.5

                    if event.key == self.map["left"]:
                        if self.speed[0] > 0: self.speed[0] = 0
                        if self.speed[0] > -3: self.speed[0] -= 0.5
                    elif event.key == self.map["right"]:
                        if self.speed[0] < 0: self.speed[0] = 0
                        if self.speed[0] < 3: self.speed[0] += 0.5
                if event.type == pygame.JOYAXISMOTION and event.instance_id == self.number - 1:
                    if event.axis == 0 :
                        self.speed[0] = event.value
                    if event.axis == 1 :
                        self.speed[1] = event.value


    class ComType(Movable):
        pass

    class PuckType(Movable):
        pass

    class Immuable:
        def __init__(self, x, y, texture="Goal.jpg"):
            self.tex = pygame.image.load(texture).convert()
            self.rect = self.tex.get_rect()

            self.rect.x = x
            self.rect.y = y

            self.innerscore = 0

        def GoalCheck(self, puckr):

            if self.rect.colliderect(puckr):
                self.innerscore += 1
                print("GOOOOOOOOOOAL!")
                print("Player 1 Score =", goal2.innerscore)
                print("player 2 Score =", goal1.innerscore)
                if events!=[]: print(events)
                return 0
            return 1


    pygame.init()
    size = width, height = 1366, 768
    screen = pygame.display.set_mode(size)
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

    #pygame.time.Clock()

    goal1 = Immuable(0, (height * 0.5) - 100)
    goal2 = Immuable(width - 20, (height * 0.5) - 100)

    misc_text = pygame.font.SysFont('Calibri', 30)

    while goal1.innerscore < 3 and goal2.innerscore < 3:

        player1 = PlayerType(width/6, height/2, 10, "keyboard1")
        player1.number = 1
        player2 = PlayerType(5*width/6, height/2, 10, "keyboard2")
        player2.number = 2
        puck1 = PuckType(width/2, height/2, 5, "0", "intro_ball.gif")

        players = [player2, player1]
        entities = [player2, player1, puck1]
        print(entities)
        entities[0], entities[2] = entities[2], entities[0]
        print(entities)

        loop = 1

        while loop:

            print(pygame.time.get_ticks())
            for entity in entities:
                entity.boundary_check()

            puck1.physics_check([player1, player2])
            player1.physics_check([puck1, player2])
            player2.physics_check([puck1, player1])

            for entity in entities:
                entity.run()

            events = pygame.event.get()
            #if events!=[]: print(events)
            player1.get_inputs(events)
            player2.get_inputs(events)

            loop *= goal1.GoalCheck(puck1.rect)
            loop *= goal2.GoalCheck(puck1.rect)

            score1 = misc_text.render("Player 1 : " + str(goal2.innerscore), False, black)
            score2 = misc_text.render("Player 2 : " + str(goal1.innerscore), False, black)
            #fps_count = misc_text.render("FPS=" + str(pygame.time.Clock.get_fps()), False, black)

            playtag1 = misc_text.render("P1", False, blue)
            playtag2 = misc_text.render("P2", False, red)

            screen.fill(white)
            screen.blit(player1.tex, player1.rect)
            screen.blit(player2.tex, player2.rect)
            screen.blit(puck1.tex, puck1.rect)

            screen.blit(goal1.tex, goal1.rect)
            screen.blit(goal2.tex, goal2.rect)

            screen.blit(score1, (20, 0))
            screen.blit(score2, (width-200, 0))
            #screen.blit(fps_count, (0, 0))

            screen.blit(playtag1, (player1.rect.x - 15, player1.rect.y - 15))
            screen.blit(playtag2, (player2.rect.x - 15, player2.rect.y - 15))

            pygame.display.flip()

    if goal1.innerscore < goal2.innerscore:
        winner = "Player 1"
    else:
        winner = "Player 2"

    print(winner, "wins.")

    end_message = misc_text.render(str(winner)+" Wins! GAME OVER", False, red)
    screen.blit(end_message, (width/3, height/2))
    pygame.display.flip()

    sleep(5)
