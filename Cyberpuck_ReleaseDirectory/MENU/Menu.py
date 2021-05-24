import pygame
import sys
from MENU.Application import Application

from SOLO.campaign_manager import complete_campaign

class Menu(Application):
    def __init__(self, game):
        Application.__init__(self, game)
        
        #we have to state the very first text that the user can select
        self.state = "Story"
        
        #this is helpful to determine the different positions of the texts
        self.storyx, self.storyy = self.midw + 300, self.midh - 30
        self.versusx, self.versusy = self.midw + 300, self.midh +40
        self.collectionx, self.collectiony = self.midw + 300, self.midh + 110
        self.settingsx, self.settingsy = self.midw + 300, self.midh + 110
        self.creditsx, self.creditsy = self.midw + 300, self.midh + 180
        self.quitx, self.quity = self.midw + 300, self.midh + 250
        self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)

        #this will define the images that can be loaded in the file
        self.back = pygame.image.load('MENU\Back_Menu.png')
        self.logo1 = pygame.image.load('MENU\logo1.png').convert_alpha()
        self.logo_game = pygame.image.load('MENU\logo.png').convert_alpha()

        pygame.display.set_icon(self.logo1)

    #this function display_menu will help us to show the different options that we can choose for the menu and display a graphic part
    def display_menu(self):
        self.run_display = True
        pygame.mixer.music.load('MENU\midnight-ride-01a.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        while self.run_display:
            self.game.check_events()
            self.check_input()
            
            #this will show the differents images for the menu (the backgorund and the logo) and of course the different texts
            self.game.background(self.back)
            self.game.draw_logo_game(self.logo_game)
            self.game.draw_text_2('Menu', 60, self.game.width - 375, self.game.height - 600)
            self.game.draw_text("Story", 40, self.storyx, self.storyy)
            self.game.draw_text("Versus", 40, self.versusx, self.versusy)
            self.game.draw_text("Collection", 40, self.collectionx, self.collectiony)
            #self.game.draw_text("Settings", 40, self.settingsx, self.settingsy)
            self.game.draw_text("Credits", 40, self.creditsx, self.creditsy)
            self.game.draw_text_2("Quit", 40, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()


    #this function move_cursor can allow the user to select the option they want by using the keyboard keys
    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.play_sfx(r'MENU\button-3.wav')
            if self.state == 'Story':
                self.cursor_rect.midtop = (self.versusx + self.offset, self.versusy)
                self.state = 'Versus'
            elif self.state == 'Versus':
                self.cursor_rect.midtop = (self.collectionx + self.offset, self.collectiony)
                self.state = 'Collection'
            elif self.state == 'Collection':
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.creditsy)
                self.state = 'Credits'
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
            self.play_sfx(r'MENU\button-3.wav')
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
                self.state = 'Collection'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    #this function is helpful since the user can activate the option they want selecting it and using the enter key from the keyboard
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Story':
                self.play_sfx(r'MENU\button-11.wav')
                complete_campaign(self.game.system_parameters)
                self.game.playing = True
            elif self.state == 'Versus':
                self.play_sfx(r'MENU\button-11.wav')
                self.game.curr_menu = self.game.versus
            elif self.state == 'Collection':
                self.play_sfx(r'MENU\button-11.wav')
                self.game.curr_menu = self.game.collection
            elif self.state == 'Settings':
                self.play_sfx(r'MENU\button-11.wav')
                self.game.curr_menu = self.game.settings
            elif self.state == 'Credits':
                self.play_sfx(r'MENU\button-11.wav')
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit':
                self.play_sfx(r'MENU\button-4.wav')
                #self.game.curr_menu = self.game.quit
                sys.exit()
            self.run_display = False
