import pygame
import winsound
from CyberPuck3.Game import Game
from CyberPuck3.Splash import Splash

width = 1366
height = 768

start = Splash()
start.screen()

while start.statut:

    tkey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if tkey[pygame.K_RETURN]:
            app = Game()
            winsound.PlaySound('button-2.wav', winsound.SND_FILENAME)

            while app.running:
                app.curr_menu.display_menu()
                app.game_loop()

pygame.quit()