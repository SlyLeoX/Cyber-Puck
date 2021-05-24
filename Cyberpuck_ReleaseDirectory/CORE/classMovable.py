import pygame
import numpy as np

from CORE.auxiliary_Stats import return_charstats


class Movable:

    def __init__(self, x, y, infopack):
        # TODO: The following  static string shall be replace by some function answer if we have multiple tex.
        # Load and resize the image of the puck.
        self.tex = pygame.image.load(r"CORE\ressources\misc\puck_alt.png").convert_alpha()
        self.tex = pygame.transform.scale(self.tex, (111, 111))
        self.rect = self.tex.get_rect()

        # Used by some functions as an identification medium.
        self.base_x = x

        # In the following, there are True_pos and the rect.x rect.y pair:
        # True_pos contains float values and the pair can only hold integers.
        # To keep track of the precise position allow the use of non-integer speeds for better physics precision.
        self.speed_multiplier = [1, 1]
        self.speed = [0, 0]
        self.true_pos = [x, y]
        # The ray of the object's image is used for physics verification.
        self.ray = self.rect.size[0] / 2

        self.rect.x = x
        self.rect.y = y

        # Mass is a parameter linked to the chosen character that is used for physics calculation.
        self.mass = return_charstats(infopack[1])[0]

        # This value may be used by an effect to disable collisions in certain circumstances.
        self.tangible = True

        # Those two are used in physics calculation to avoid certain errors.
        self.last_impact = 0
        self.followed_impact = 0

    # Displace the objects on the screen according to the objects' speed on x and y axis.
    # The function also manage the terrain friction parameters:
    # The speed of the object slowly diminishes according to the terrain's roughness parameter.
    def run(self, resistance=100):
        # Speed reduction is applied successively to x and y axis.
        for i in range(2):

            if self.speed[i] < 0:
                self.speed[i] += 1/resistance

            elif self.speed[i] > 0:
                self.speed[i] -= 1/resistance

        # The speed multiplier parameter comes from some effects, and may reduce or increase speeds.
        for i in range(2):
            self.true_pos[i] += (self.speed[i])*self.speed_multiplier[i]

        # Pygame automatically convert rect.x and rect.y values to integers.
        self.rect.x = self.true_pos[0]
        self.rect.y = self.true_pos[1]

    # Concentrates all the collision physics operations.
    def physics_check(self, entities):
        for entity in entities:
            # We verify we don't try to detect the collision of an object with itself.
            if self.rect.centerx == entity.rect.centerx and self.rect.centery == entity.rect.centery:
                continue

            # DEBUG CODE (WIP)

            # This part of the code counts the successive collisions of an object.
            if (self.rect.centerx - entity.rect.centerx) ** 2 + (self.rect.centery - entity.rect.centery) ** 2 < (
                    self.ray + entity.ray) ** 2 and (pygame.time.get_ticks() - self.last_impact <= 2):
                self.followed_impact += 2
                # print("FOLLOWED IMPACT!", self.followed_impact)
            elif self.followed_impact > 0:
                # print("DEBUG DEFUSED!")
                self.followed_impact -= 1

            # If an object makes too many successive collisions each frame, the code will try to move it from there.
            if self.followed_impact >= 8:
                # print("DEBUG TRIGGERED!")
                if self.true_pos[0] < entity.true_pos[0]:
                    self.true_pos[0] -= 3
                else:
                    self.true_pos[0] += 3
                self.followed_impact = 0

            # Part of the debugs : Diminish speeds when they got too high.
            for test in [self,entity]:
                for i in range(2):
                    if test.speed[i] > 15:
                        test.speed[i] = 10
                    if test.speed[i] < -15:
                        test.speed[i] = -10

            # Forbid an entity to have multiple collision in (4) consecutive frames.
            # Used to avoid collision bugs.
            cooldown_argument = (
                    pygame.time.get_ticks() - self.last_impact > 4 and pygame.time.get_ticks() - entity.last_impact > 4)

            # The following if detects collisions by checking displacement between two objects' centers.
            if (self.rect.centerx - entity.rect.centerx) ** 2 + (self.rect.centery - entity.rect.centery) ** 2 <= (
                    self.ray + entity.ray) ** 2 and cooldown_argument:

                a = self
                b = entity

                # Takes account that a collision just happened.
                self.last_impact = pygame.time.get_ticks()
                entity.last_impact = pygame.time.get_ticks()

                # We compute relative speed for use further in the code.
                relative_v = [a.speed[0] - b.speed[0], a.speed[1] - b.speed[1]]

                # The if situation is an exception case for which the classic equation would not work.
                if a.rect.centerx == b.rect.centerx:

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

                # We make one of the object advance to reduce multiple-collisions bugs.
                a.run()

                # A collision awards "special technique" point to players implicated in the colliding.
                if type(a).__name__ != "PlayerType" and type(a).__name__!="AiType":
                    if b.current_special < b.max_special: b.current_special += 0.5
                elif type(b).__name__ != "PlayerType" and type(b).__name__!="AiType":
                    if a.current_special < a.max_special: a.current_special += 0.5

                # Returns the average position of the objects to allow the display of a visual effect.
                return ((a.rect.x+b.rect.x)/2,(a.rect.y+b.rect.y)/2)
        return 0

    # Checks that no object is outside of the terrain.
    def boundary_check(self, size):

        if 1:
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

        # We return the side on which the border collision happened to allow the display of a visual effect.
        return w