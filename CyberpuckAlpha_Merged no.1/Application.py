import pygame

width = 1366
height = 768

class Application():
    def __init__(self, game):
        self.game = game
        self.midw, self.midh = self.game.width / 2, self.game.height / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 220, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)
        #pygame.draw.rect(self.game.window2, self.game.RED, (self.cursor_rect.x, self.cursor_rect.y, 200, 100), 2)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()