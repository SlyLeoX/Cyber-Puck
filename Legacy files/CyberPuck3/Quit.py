from CyberPuck3.Application import Application

class Quit(Application):
    def __init__(self, game):
        Application.__init__(self, game)

    def quit(self):
        self.run_display = False