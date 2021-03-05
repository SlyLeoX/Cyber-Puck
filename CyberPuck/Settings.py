import pygame

width = 1366
height = 768

class Settings:

    def __init__(self, game):
        self._fenetre = game.fenetre
        game.fond = (0, 0, 0)

        from itertools import cycle
        colors = [(0, 48, i) for i in range(0, 256, 15)]
        colors.extend(sorted(colors[1:-1], reverse=True))
        self.TextColor = cycle(colors)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.TextSettings()

        self.rectTexte = self.text.get_rect()
        self.rectTexte.center = (width / 2, height / 2)

    def TextSettings(self):
        TextDisplay = pygame.display.set_mode((width, height))

        color = (0, 0, 0)
        color1 = (200, 0, 0)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Settings still in working', True, color1)

        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2)

        while True:
            TextDisplay.fill(color)
            TextDisplay.blit(text, text_rect)

            pygame.display.update()

    def update(self, events):
        self._fenetre.blit(self.text, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.TextSettings()
                break

    def destroy(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)