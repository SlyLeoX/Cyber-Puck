import pygame
import numpy as np

from classMovableControlsAux import controls_mapping


class Movable:

    def __init__(self, x, y, mass, keys, texture="bumper.gif"):
        self.tex = pygame.image.load(texture).convert()
        self.rect = self.tex.get_rect()

        self.speed = [0, 0]
        self.true_pos = [x, y]
        self.ray = self.rect.size[0] / 2

        self.rect.x = x
        self.rect.y = y

        self.mass = mass
        self.map = controls_mapping(keys)

        self.last_impact = 0
        self.number = -1

        self.score=0
        self.current_inputs = [0,0]

        self.followed_impact = 0
        #Faut que je comprenne comment marche le mélange entre héritages et inits...

    def run(self, resistance=500):

        # if rd.randint(0, resistance) == resistance:
        # print("Slow down!")

        for dat_speed in self.speed:
            if dat_speed > 0:
                dat_speed -= 1 / resistance
            elif dat_speed < 0:
                dat_speed += 1 / resistance
            dat_speed = 0 if abs(dat_speed) < 0.1 else 0

        # rect = {1: self.rect.x, 2: self.rect.y}
        for i in range(0, 2):
            self.true_pos[i] += self.speed[i]
            # if self.true_pos != [0, 0]: print(self.true_pos)
            # rect[i] = self.true_pos[i]

        self.rect.x = self.true_pos[0]
        self.rect.y = self.true_pos[1]
        # self.rect = self.rect.move(self.speed[0], self.speed[1])

    def physics_check(self, entities):
        # print("Check before moving")
        for entity in entities:
            if self.rect.centerx == entity.rect.centerx and self.rect.centery == entity.rect.centery:
                continue

            # DEBUG CODE (WIP)
            if (self.rect.centerx - entity.rect.centerx) ** 2 + (self.rect.centery - entity.rect.centery) ** 2 < (
                    self.ray + entity.ray) ** 2 and (pygame.time.get_ticks() - self.last_impact <= 2):
                self.followed_impact += 2
                print("FOLLOWED IMPACT!",self.followed_impact)
            elif self.followed_impact > 0:
                print("DEBUG DEFUSED!")
                self.followed_impact -=1

            if self.followed_impact >= 8:
                print("DEBUG TRIGGERED!")
                if self.true_pos[0] < entity.true_pos[0]:
                    self.true_pos[0] -= 3
                else:
                    self.true_pos[0] += 3
                self.followed_impact = 0



            # if self.rect.colliderect(lentity.rect) and (pygame.time.get_ticks()-self.last_impact > 16 or pygame.time.get_ticks()-lentity.last_impact > 16 ):
            if (self.rect.centerx - entity.rect.centerx) ** 2 + (self.rect.centery - entity.rect.centery) ** 2 <= (
                    self.ray + entity.ray) ** 2 and (
                    pygame.time.get_ticks() - self.last_impact > 1 or pygame.time.get_ticks() - entity.last_impact > 1):

                a = self
                b = entity

                # a, b = self, lentity

                self.last_impact = pygame.time.get_ticks()
                entity.last_impact = pygame.time.get_ticks()

                relative_v = [a.speed[0] - b.speed[0], a.speed[1] - b.speed[1]]

                if a.rect.centerx == b.rect.centerx:  # temporary patch (Romeo knows da way ! )

                    b.speed[1] = a.speed[1] * round(b.mass / a.mass)

                else:  # Proper physics calculated.

                    c = (a.rect.centery - b.rect.centery) / (a.rect.centerx - b.rect.centerx)
                    s = (relative_v[0]) * (np.cos(np.tan(c))) + (relative_v[1]) * (np.sin(np.tan(c)))

                    va = s - ((2 * s * b.mass) / (a.mass + b.mass))
                    vb = ((2 * s * a.mass) / (a.mass + b.mass))

                    a.speed[0] = va * (np.cos(np.tan(c))) + b.speed[0]
                    a.speed[1] = va * (np.sin(np.tan(c))) + b.speed[1]

                    b.speed[0] = vb * (np.cos(np.tan(c))) + b.speed[0]
                    b.speed[1] = vb * (np.sin(np.tan(c))) + b.speed[1]

                #print(self.speed, lentity.speed)

                a.run()
                b.run()
                # while (self.rect.centerx - lentity.rect.centerx)**2 + (self.rect.centery - lentity.rect.centery)**2 < (self.ray + lentity.ray)**2:
                # b.run()
                # b.boundary_check()

                # print("IMPACT", self, lentity, lentity.dspeed[0], lentity.dspeed[1])
                # self.speed[1], lentity.speed[1] = lentity.speed[1], self.speed[1]
                # self.speed[0], lentity.speed[0] = lentity.speed[0], self.speed[0]
                # self.rect = self.rect.move(self.speed)

                return 1
        return 0

    def boundary_check(self, size):

        if 1:
            # print("Check before moving.")
            w = 0
            if self.rect.left <= 0:
                self.rect.x += 5
                self.true_pos[0] += 5
                self.speed[0] *= -1
                w = 1

            if self.rect.right >= size[0]:
                self.rect.x -= 5
                self.true_pos[0] -= 5
                self.speed[0] *= -1
                w = 1

            if self.rect.top <= 0:
                self.true_pos[1] += 5
                self.rect.y += 5
                self.speed[1] *= -1
                w = 1

            if self.rect.bottom >= size[1]:
                self.true_pos[1] -= 5
                self.rect.y -= 5
                self.speed[1] *= -1
                w = 1

            if w: self.last_impact = pygame.time.get_ticks()