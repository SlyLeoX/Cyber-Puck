from MENU.Application import Application

#this class file will be used to quit the game
class Quit(Application):
    def __init__(self, game):
        Application.__init__(self, game)

    def quit(self):
        self.run_display = False
