import pygame
import winsound
from CyberPuck3.Application import Application

class Menu(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        self.state = "Story"
        self.storyx, self.storyy = self.midw + 300, self.midh - 100
        self.versusx, self.versusy = self.midw + 300, self.midh - 30
        self.collectionx, self.collectiony = self.midw + 300, self.midh + 40
        self.settingsx, self.settingsy = self.midw + 300, self.midh + 110
        self.creditsx, self.creditsy = self.midw + 300, self.midh + 180
        self.quitx, self.quity = self.midw + 300, self.midh + 250
        self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)

        self.back = pygame.image.load('Back_Menu.png')
        self.logo1 = pygame.image.load('logo1.png')
        self.logo_game = pygame.image.load('logo.png')

        pygame.display.set_icon(self.logo1)

    def display_menu(self):
        self.run_display = True
        pygame.mixer.music.load('midnight-ride-01a.wav')
        pygame.mixer.music.play(-1)
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.background(self.back)
            self.game.draw_logo_game(self.logo_game)
            #self.game.draw_text_3('Made by', 50, 320, 565)
            #self.game.draw_text_2('Copper Gears', 60, 360, 650)
            self.game.draw_text_2('Menu', 60, self.game.width - 375, self.game.height - 600)
            self.game.draw_text("Story", 40, self.storyx, self.storyy)
            self.game.draw_text("Versus", 40, self.versusx, self.versusy)
            self.game.draw_text("Collection", 40, self.collectionx, self.collectiony)
            self.game.draw_text("Settings", 40, self.settingsx, self.settingsy)
            self.game.draw_text("Credits", 40, self.creditsx, self.creditsy)
            self.game.draw_text_2("Quit", 40, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == 'Story':
                self.cursor_rect.midtop = (self.versusx + self.offset, self.versusy)
                self.state = 'Versus'
            elif self.state == 'Versus':
                self.cursor_rect.midtop = (self.collectionx + self.offset, self.collectiony)
                self.state = 'Collection'
            elif self.state == 'Collection':
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = 'Settings'
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)
                self.state = 'Story'

        elif self.game.UP_KEY:
            winsound.PlaySound('button-3.wav', winsound.SND_FILENAME)
            if self.state == 'Story':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Versus':
                self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)
                self.state = 'Story'
            elif self.state == 'Collection':
                self.cursor_rect.midtop = (self.versusx + self.offset, self.versusy)
                self.state = 'Versus'
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.collectionx + self.offset, self.collectiony)
                self.state = 'Collection'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = 'Settings'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Story':
                winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.playing = True
            elif self.state == 'Versus':
                winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.versus
            elif self.state == 'Collection':
                winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.collection
            elif self.state == 'Settings':
                winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.settings
            elif self.state == 'Credits':
                winsound.PlaySound('button-11.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit':
                winsound.PlaySound('button-4.wav', winsound.SND_FILENAME)
                self.game.curr_menu = self.game.quit
            self.run_display = False