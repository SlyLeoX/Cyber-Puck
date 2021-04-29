import pygame
import numpy as np

# example_input: (60,"dash2,attraction2") <=> (for 60 frames (1sec) player goes 2 times faster


class EffectType:

    def __init__(self, player, lenght, effects, game):

        self.origin = pygame.time.get_ticks()
        self.lenght = lenght

        self.types = effects
        self.types = self.types.split(",")
        print(self.types)
        self.player = player
        print("You are", self.player.charname)

        screen = game.screen
        self.puck = game.base_entities[0]

        for searching in game.players:
            if searching.number != self.player.number:
                self.opponent = searching
                print("The opponent is", self.opponent.charname)

        print("Most definitely starting something")
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

    def ultra_panorama(self, player, screen):
        print("Actively blitting some Noice Sanic !")

        screen_dim = (screen[0], screen[1])

        part = (pygame.time.get_ticks()-self.origin)/1000

        icon = pygame.image.load(player.icon).convert_alpha()
        icon = pygame.transform.scale(icon, [round(screen_dim[0] / 2), round(screen_dim[1] / 2)])

        screen[2].blit(icon, (part*screen_dim[0], screen_dim[1] / 3))

    def speedUp(self, target, amp):
        for i in range(2):
            self.player.speed_multiplier[i]=int(amp)

    def speedRestore(self, target):
        print(target.speed_multiplier)
        for i in range(2):
            target.speed_multiplier[i] = 1
        print(target.speed_multiplier)

    def speedDown(self, target, amp):
        for i in range(2):
            target.speed_multiplier[i] = 1/int(amp)

    def getDownMrPresident(self, screen_dim):

        m = (self.player.rect.y - screen_dim[1]/2) / (self.player.rect.x - screen_dim[0]*10/12)
        print(-np.cos(np.arctan(m)) * 15, np.sin(np.arctan(m)) * 15)
        self.player.speed[0] = -np.cos(np.arctan(m)) * 15
        self.player.speed[1] = np.sin(np.arctan(m)) * 15

    def last_frame(self):
        if pygame.time.get_ticks() >= self.origin + self.lenght:
            print("Ahoy!")
            return True
        return False

    def effects_apply(self, player, screen, entities):
        for effect in self.types:
            print(effect[:-1])

            if effect[:-1] == "ultra" and pygame.time.get_ticks()-self.origin < 1000:
                self.ultra_panorama(player, screen)

            if self.last_frame():
                print("Most definitely ending something")

                if effect[:-1] == "self_speedup":
                    self.speedRestore(self.player)

                if effect[:-1] == "puck_speedup":
                    print("puck speedup offline! 1")
                    self.speedRestore(self.puck)

                if effect[:-1] == "enemy_speeddown":
                    self.speedRestore(self.opponent)

            else:

                if effect[:-1] == "attraction":
                    pass
