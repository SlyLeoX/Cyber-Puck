import pygame
import numpy as np

# example_input: (60,"dash2,attraction2") <=> (for 60 frames (1sec) player goes 2 times faster

# The effect type only stores active character techniques launched by the players.
# These techniques have a lenght and list of effects to apply.
class EffectType:

    def __init__(self, player, lenght, effects, game):

        # We store the number of frames the effects lasts and the "date" of beginning.
        self.origin = pygame.time.get_ticks()
        self.lenght = lenght

        self.types = effects
        self.types = self.types.split(",")
        #print(self.types)
        self.player = player
        #print("You are", self.player.charname)

        screen = game.screen
        self.puck = game.base_entities[0]

        # The following code attempts to determine which object is the opponent and store it.
        for searching in game.players:
            if searching.number != self.player.number:
                self.opponent = searching
                #print("The opponent is", self.opponent.charname)

        # We ignite every effect that start at the creation of the object
        for effect in self.types:
            if effect[:-1] == "self_speedup":
                self.speedUp(self.player, self.types[-1:])

            if effect[:-1] == "puck_speedup":
                self.speedUp(self.puck, effect[-1:])

            if effect[:-1] == "enemy_speeddown":
                self.speedDown(self.opponent, effect[-1:])

        # Alexander's "Get Down Mr President"
            if effect[:-1] == "gdmp":
                print("GET DOWN MISTER PRESIDENT!")
                self.getDownMrPresident((game.width, game.height))

    # The following code creates a visual effect with the character's portait when a ultra attack i launched.
    def ultra_panorama(self, player, screen):
        # The portait is printed at a position going from left to right fast as frames passes.
        screen_dim = (screen[0], screen[1])

        part = (pygame.time.get_ticks()-self.origin)/1000

        icon = pygame.image.load(player.icon).convert_alpha()
        icon = pygame.transform.scale(icon, [round(screen_dim[0] / 2), round(screen_dim[1] / 2)])

        screen[2].blit(icon, (part*screen_dim[0], screen_dim[1] / 3))

    # Allow to increase speed by a given factor of an actor.
    def speedUp(self, target, amp):
        for i in range(2):
            self.player.speed_multiplier[i]=int(amp)
    # Allow to get the speed of an object back to normal.
    def speedRestore(self, target):
        print(target.speed_multiplier)
        for i in range(2):
            target.speed_multiplier[i] = 1
        print(target.speed_multiplier)

    # Allow to decrease speed by a given factor of an actor.
    def speedDown(self, target, amp):
        for i in range(2):
            target.speed_multiplier[i] = 1/int(amp)

    def getDownMrPresident(self, screen_dim):
        # Similar code to the IA lvl 1, launches the player towards its goals.
        m = (self.player.rect.y - screen_dim[1]/2) / (self.player.rect.x - screen_dim[0]*10/12)
        print(-np.cos(np.arctan(m)) * 15, np.sin(np.arctan(m)) * 15)
        self.player.speed[0] = -np.cos(np.arctan(m)) * 15
        self.player.speed[1] = np.sin(np.arctan(m)) * 15

    # Allows to detect when an effect should be ended.
    def last_frame(self):
        if pygame.time.get_ticks() >= self.origin + self.lenght:
            print("Ahoy!")
            return True
        return False

    # Applies or removes effects of techniques that are over.
    def effects_apply(self, player, screen, entities):
        for effect in self.types:
            print(effect[:-1])

            if effect[:-1] == "ultra" and pygame.time.get_ticks()-self.origin < 1000:
                self.ultra_panorama(player, screen)

            # Removing effects of techniques that are ending.
            if self.last_frame():

                if effect[:-1] == "self_speedup":
                    self.speedRestore(self.player)

                if effect[:-1] == "puck_speedup":
                    print("puck speedup offline! 1")
                    self.speedRestore(self.puck)

                if effect[:-1] == "enemy_speeddown":
                    self.speedRestore(self.opponent)

            else:
                # Example of an effect that would attract objects and therefore be applied each frame.
                # The attraction effect is not used though.
                if effect[:-1] == "attraction":
                    pass
