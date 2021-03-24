import pygame

#example_input: (60,"dash2,attraction2") <=> (for 60 frames (1sec) player goes 2 times faster

class effectType:

    def __init__(self, player,lenght, effects):

        self.origin = pygame.time.get_ticks()
        self.lenght = lenght

        self.types = effects
        print("Teratop")
        self.types = self.types.split(",")
        print(self.types)
        self.player = player

        #Here while I have not resolved framerate related issues.
        self.initialized = False

    def ultra_panorama(self, player, screen):

        print("Actively blitting some Noice Sanic !")
        screen_dim = (screen[0],screen[1])

        part = (pygame.time.get_ticks()-self.origin)/1000

        icon = pygame.image.load(player.icon).convert()
        icon = pygame.transform.scale(icon, [round(screen_dim[0] / 2), round(screen_dim[1] / 2)])

        screen[2].blit(icon, (screen_dim[0]*1/4 + part*1/3*screen_dim[0], screen_dim[1] / 3))

    def speedUp(self, amp):
        for i in range(2):
            self.player.speed[i]*=amp

    def speedDown(self, amp):
        for i in range(2):
            self.player.speed[i] /= amp

    def first_frame(self):
        if self.initialized == False:
            self.initialized = True
            return True
        return False

    def last_frame(self):
        if pygame.time.get_ticks() >= self.origin + self.lenght:
            print("Ahoy!")
            return True
        return False

    def effects_apply(self, player, screen):
        for effect in self.types:
            print(effect[:-1])

            if effect[:-1] == "ultra" and pygame.time.get_ticks()-self.origin < 1000:
                self.ultra_panorama(player, screen)

            if self.first_frame():
                print("Most definitely starting something")
                if effect[:-1]=="speed":
                    self.speedUp(effect[-1:])

            if self.last_frame():
                print("Most definitely ending something")
                if effect[:-1]=="speed":
                    self.speedDown(effect[-1:])

            else:

                if effect[:-1] == "attraction":
                    pass

