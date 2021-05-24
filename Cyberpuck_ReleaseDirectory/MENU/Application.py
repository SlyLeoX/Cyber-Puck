import pygame

width = 1366
height = 768

#this class is on the most important in the MENU folder since this file will be called by most of all the class present in the folder
class Application():
    def __init__(self, game):
        self.game = game
        self.midw, self.midh = self.game.width / 2, self.game.height / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 220, 20)
        self.offset = - 100

    #the function draw_cursor is an important function that will help the user to choose the option he wants (graphically)
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def play_sfx(self, path):
        effect = pygame.mixer.Sound(path)
        effect.set_volume(0.3)
        effect.play()
