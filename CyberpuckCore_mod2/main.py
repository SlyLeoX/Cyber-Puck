#Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)
#Version 1.2a : Première introduction des controles au joystick + Fixs physiques divers, abandon de la var TrueCenter.

import pygame

from classOneGame import partyOn

white = 255, 255, 255
black = 0, 0, 0
red = 255, 65, 65
blue = 65, 65, 255

if __name__ == '__main__':

    pygame.init()
    size = width, height = 1366, 768
    screen = pygame.display.set_mode(size)

    system_parameters = [screen, 1366, 768]
    player_parameters = [["PLAYER1", "keyboard1", "bumper.gif"], ["COM", "COM1", "bumper.gif"]]

    game = partyOn(system_parameters,player_parameters)
    gp1,gp2=game.players[0],game.players[1]

    while gp1.score < 3 and gp2.score < 3:

        game.entities_reset()

        loop = 1
        while loop:

            game.complete_frame()
            game.get_allinputs()

            loop = game.goal_verif()

            screen.fill(white)
            game.blit_entities()
            game.blit_stadium()
            game.blit_scores()
            game.blit_playtags()

            pygame.display.flip()







