import pygame

width = 1200
height = 800

class Settings:

    def __init__(self, jeu):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self.TextColor = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.TextSettings()
        self.rectTexte = self.text.get_rect()
        self.rectTexte.center = (width / 2, height / 2)
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

    def TextSettings(self):
        self.text = self._font.render('Settings still in working', True, next(self.TextColor))

    def update(self, events):
        self._fenetre.blit(self.text, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.TextSettings()
                break

    def destroy(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)