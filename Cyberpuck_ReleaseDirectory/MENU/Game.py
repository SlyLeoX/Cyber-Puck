import pygame
from MENU.Menu import Menu
from MENU.Versus import Versus
from MENU.Collection import Collection
from MENU.Characters import Characters
from MENU.Play import Play
from MENU.Pucks import Pucks
from MENU.Selection import Selection
from MENU.Settings import Settings
from MENU.Credits import Credits
from MENU.Quit import Quit

#this file is very important because the functions present in this file will be called in the other files 
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.Z_KEY, self.S_KEY, self.TAB_KEY = False, False, False

        self.width, self.height = 1366, 768
        self.display = pygame.Surface((self.width,self.height))
        self.window = pygame.display.set_mode(((self.width,self.height)))

        self.system_parameters = [self.window,[self.width,self.height]]

        #this is helpful because it will be served to define the form and the color of the texts
        self.font_name = 'MENU\8-BIT WONDER.TTF'
        self.colors = dict(normal=(255, 255, 255), survol=(0, 0, 0))
        self.BLACK = (0, 0, 0)
        self.RED = (200, 0, 0)
        self.WHITE = (255, 255, 255)

        #here we list the files to call them later in different calls  
        self.menu = Menu(self)
        self.versus = Versus(self)
        self.collection = Collection(self)
        self.characters = Characters(self)
        self.play = Play(self)
        self.pucks = Pucks(self)
        self.selection = Selection(self)
        self.settings = Settings(self)
        self.credits = Credits(self)
        self.quit = Quit(self)
        self.curr_menu = self.menu

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

                if event.key == pygame.K_z:
                    self.Z_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True
                if event.key == pygame.K_TAB:
                    self.TAB_KEY = True
            if event.type == pygame.K_CLEAR:
                print('ahhhh')

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.Z_KEY, self.S_KEY, self.TAB_KEY = False, False, False

        
    #here is the definition of functions to show texts on the screen
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.colors['normal'])
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_2(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.RED)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_3(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

        
    #this function is helpful to set a image as background
    def background(self, image):
        self.display.blit(image, (0, 0))

    #all the functions below are helpful to display an image at certain positions
    def draw_logo_game(self, image):
        self.display.blit(image, (100, 100))

    def draw_perso1(self, image):
        self.display.blit(image, (350, 225))

    def draw_perso2(self, image):
        self.display.blit(image, (750, 225))

    def draw_puck1(self, image):
        self.display.blit(image, (350, 225))

    def draw_puck2(self, image):
        self.display.blit(image, (750, 225))

    def draw_puck1(self, image):
        self.display.blit(image, (200, 225))

    def draw_puck1(self, image):
        self.display.blit(image, (200, 225))

    def draw_logo_efrei(self, image):
        self.display.blit(image, (125, 275))
