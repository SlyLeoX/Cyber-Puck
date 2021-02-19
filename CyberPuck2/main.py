import pygame
from CyberPuck2.Application import Application

width = 1366
height = 768

app = Application()
app.menu()


clock = pygame.time.Clock()



while app.statut:
    tkey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if tkey[pygame.K_TAB]:
            print("tab")

    app.update()
    clock.tick(30)

pygame.quit()