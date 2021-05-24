import pygame

width = 1366
height = 768

class Splash:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CyberPuck")

        self.clock = pygame.time.Clock()

        self.display = pygame.Surface((width,height))
        self.window = pygame.display.set_mode((width, height))
        self.statut = True

        self.logo1 = pygame.image.load('MENU\logo2.png')
        self.back = pygame.image.load('MENU\Back_Menu.png')

        pygame.display.set_icon(self.logo1)

    def screen(self):
        RED = (200, 0, 0)
        font = pygame.font.Font('MENU\8-BIT WONDER.TTF', 30)

        text = font.render('Press Enter to start the game', True, RED)
        text_rect = text.get_rect()
        text_rect.center = (width/2, 600)

        self.window.blit(self.back, (0, 0))
        self.window.blit(self.logo1, (450, 100))
        self.window.blit(text, text_rect)

        pygame.display.update()