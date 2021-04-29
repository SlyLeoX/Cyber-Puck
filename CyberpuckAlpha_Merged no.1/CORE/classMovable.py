import pygame
import numpy as np

from CORE.auxiliary_Stats import return_charstats


class Movable:

    def __init__(self, x, y, infopack):
        # The following  static string shall be replace by some function answer if we have multiple tex. avb.
        self.tex = pygame.image.load(r"CORE\ressources\misc\intro_ball.gif").convert()
        self.rect = self.tex.get_rect()

        self.base_x = x

        self.speed_multiplier = [1, 1]
        self.speed = [0, 0]
        self.true_pos = [x, y]
        self.ray = self.rect.size[0] / 2

        self.rect.x = x
        self.rect.y = y

        self.mass = return_charstats(infopack[1])[0]
        self.tangible = True

        self.last_impact = 0
        self.followed_impact = 0

    def run(self, resistance=100):

        # if rd.randint(0, resistance) == resistance:
        # print("Slow down!")

        for i in range(2):

            if self.speed[i] < 0:
                self.speed[i] += 1/resistance

            elif self.speed[i] > 0:
                self.speed[i] -= 1/resistance

        # rect = {1: self.rect.x, 2: self.rect.y}
        for i in range(0, 2):
            self.true_pos[i] += (self.speed[i])*self.speed_multiplier[i]
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
                # print("FOLLOWED IMPACT!", self.followed_impact)
            elif self.followed_impact > 0:
                # print("DEBUG DEFUSED!")
                self.followed_impact -= 1

            if self.followed_impact >= 8:
                # print("DEBUG TRIGGERED!")
                if self.true_pos[0] < entity.true_pos[0]:
                    self.true_pos[0] -= 3
                else:
                    self.true_pos[0] += 3
                self.followed_impact = 0

            for test in [self,entity]:
                for i in range(2):
                    if test.speed[i] > 15:
                        test.speed[i] = 10
                    if test.speed[i] < -15:
                        test.speed[i] = -10

            # Forbid an entity to have multiple collisiosn in (4) consecutive frames.
            # Used to avoid collision bugs.
            cooldown_argument = (
                    pygame.time.get_ticks() - self.last_impact > 4 and pygame.time.get_ticks() - entity.last_impact > 4)

            if (self.rect.centerx - entity.rect.centerx) ** 2 + (self.rect.centery - entity.rect.centery) ** 2 <= (
                    self.ray + entity.ray) ** 2 and cooldown_argument:

                a = self
                b = entity

                # print(a.mass)
                # print(b.mass)

                # a, b = self, lentity

                self.last_impact = pygame.time.get_ticks()
                entity.last_impact = pygame.time.get_ticks()

                relative_v = [a.speed[0] - b.speed[0], a.speed[1] - b.speed[1]]

                if a.rect.centerx == b.rect.centerx:  # temporary patch (Romeo knows da way ! )

                    b.speed[1] = a.speed[1] * (b.mass / a.mass)

                else:  # Proper physics calculated.

                    c = (a.rect.centery - b.rect.centery) / (a.rect.centerx - b.rect.centerx)
                    s = (relative_v[0]) * (np.cos(np.arctan(c))) + (relative_v[1]) * (np.sin(np.arctan(c)))

                    va = s - ((2 * s * b.mass) / (a.mass + b.mass))
                    vb = ((2 * s * a.mass) / (a.mass + b.mass))

                    a.speed[0] = va * (np.cos(np.arctan(c))) + b.speed[0]
                    a.speed[1] = va * (np.sin(np.arctan(c))) + b.speed[1]

                    b.speed[0] = vb * (np.cos(np.arctan(c))) + b.speed[0]
                    b.speed[1] = vb * (np.sin(np.arctan(c))) + b.speed[1]

                # print(self.speed, lentity.speed)
                a.run()

                # Maybe try to put it elsewhere
                if type(a).__name__ != "PlayerType" and type(a).__name__!="AiType":
                    if b.current_special < b.max_special: b.current_special += 0.5
                elif type(b).__name__ != "PlayerType" and type(b).__name__!="AiType":
                    if a.current_special < a.max_special: a.current_special += 0.5

                return ((a.rect.x+b.rect.x)/2,(a.rect.y+b.rect.y)/2)
        return 0

    def boundary_check(self, size):

        if 1:
            # print("Check before moving.")
            w = 0
            if self.rect.left <= 64*size[0]/1920:
                self.rect.x += 5
                self.true_pos[0] += 5
                self.speed[0] *= -1
                w = "left"

            if self.rect.right >= size[0]-(64*size[0]/1920):
                self.rect.x -= 5
                self.true_pos[0] -= 5
                self.speed[0] *= -1
                w = "right"

            if self.rect.top <= 132*size[1]/1080:
                self.true_pos[1] += 5
                self.rect.y += 5
                self.speed[1] *= -1
                w = "top"

            if self.rect.bottom >= size[1]-(36*size[1]/1080):
                self.true_pos[1] -= 5
                self.rect.y -= 5
                self.speed[1] *= -1
                w = "bottom"

        if w:
            self.last_impact = pygame.time.get_ticks()

        return w