#Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)
#Version 1.2a : Première introduction des controles au joystick + Fixs physiques divers, abandon de la var TrueCenter.
#1.3a: Premiere versions des barres d'endurance, de spéciale, ajout du chronomètre et des premiers mouvements spéciaux.
#1.4a: Intégration d'un overlay regroupant les informations de jeu.

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

    # Characters_stats prototype: [mass,...]
    charinfo = {"0": [5], "Sanic": [15,25,"char_icons\sanic_icon.gif"]}

    system_parameters = [screen, [1366, 768]]
    player_parameters = [["PLAYER1", charinfo["Sanic"], "keyboard1","bumper.gif"], ["PLAYER2", charinfo["Sanic"], "keyboard2", "bumper.gif"]]
    terrain = ["metal_bg.jpg", 200]

    game = partyOn(system_parameters, player_parameters, terrain)
    gp1,gp2=game.players[0], game.players[1]

    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    while gp1.score < 3 and gp2.score < 3:

        game.entities_reset()
        chrono = pygame.time.Clock()
        sec = round(pygame.time.get_ticks() / 1000)

        loop = 1
        while loop:

            chrono.tick(30)
            fps = chrono.get_fps()
            print(round(fps))

            #Chronometer_code
            if sec != round(pygame.time.get_ticks()/1000):
                sec = round(pygame.time.get_ticks()/1000)
                #print(sec//60,":", (sec//10)%6, sec%10)

            #screen.fill(white)
            game.blit_bg()

            game.get_allinputs()
            game.apply_all_effects()
            game.complete_frame()

            game.stamina_restitution()

            loop = game.goal_verif2()

            game.blit_entities()
            game.blit_stadium()

            game.blit_playtags()

            game.blit_overlay()
            game.blit_scores()
            game.blit_char_icon()
            game.blit_timer(sec)
            game.blit_stamina()
            game.blit_special()

            pygame.display.flip()







