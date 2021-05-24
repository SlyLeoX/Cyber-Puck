import pygame
from MENU.Game import Game
from MENU.Splash import Splash

width = 1366
height = 768

start = Splash()
start.screen()

while start.statut:

    tkey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if tkey[pygame.K_RETURN]:
            app = Game()
            effect = pygame.mixer.Sound(r'MENU\button-2.wav')
            effect.set_volume(0.35)
            effect.play()

            while app.running:
                app.curr_menu.display_menu()
                app.game_loop()

pygame.quit()