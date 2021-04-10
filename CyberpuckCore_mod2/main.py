# Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)
# Version 1.2a : Première introduction des controles au joystick + Fixs physiques divers, abandon de la var TrueCenter.
# 1.3a: Premiere versions des barres d'endurance, de spéciale, ajout du chronomètre et des premiers mouvements spéciaux.
# 1.4a: Intégration d'un overlay regroupant les informations de jeu.
# 1.5a: Implémentation du framework des Techniques spéciales.
# 1.6a: Début de travaux sur la refonte des inputs de jeu, optimisation des import calls, préparations au raccordement.
# 1.7a: Développement de la préintégration de l'IA dans les programmes du Core.

import pygame
from time import sleep
from classOneGame import PartyOn

white = 255, 255, 255
black = 0, 0, 0
red = 255, 65, 65
blue = 65, 65, 255

if __name__ == '__main__':

    # The following three lines will have to be erased when
    pygame.init()
    size = width, height = 1366,768
    screen = pygame.display.set_mode(size)

    # The following lines contains values that will have to be given as a parameter when calling the core.
    # Synthax: [screen,[window_width, window_height]]
    system_parameters = [screen, [width, height]]
    # Synthax for each: [Player_type(player or IA)+ID,Chosen_Character,Chosen_Peripheral,Chosen_Bumber_Texture]
    # Also called infopacks later in the code
    player_parameters = [["PLAYER1","Sanic", "keyboard1", r"ressources\misc\player_bumper.gif"],
                         ["COM2", "Alexander", "keyboard2", r"ressources\misc\player_bumper.gif"]]
    # Synthax: [gametype, terrain chosen]
    game_parameters = ["first_to3", "metal1"]

    # Supercall synthax: (system_parameters, players_parameters, chosen_stadium)
    game = PartyOn(system_parameters, player_parameters, game_parameters[1])
    gp1, gp2 = game.players[0], game.players[1]
    sec=0

    # Joysticks initialization.
    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    # Victoryloops condition.
    condition = 0
    if game_parameters[0] == "first_to3":
        condition = gp1.score < 3 and gp2.score < 3
    elif game_parameters[0] == "time_to3":
        condition = sec <= 180

    pygame.mixer.init()
    pygame.mixer.music.load(r'ressources\soundtracks\UNL Pre-Battle Theme - The Legendary Titan.wav')
    pygame.mixer.music.queue(r'ressources\soundtracks\UNL Pre-Battle Theme - Our Hisou Tensoku.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    while gp1.score < 3 and gp2.score < 3:

        game.entities_reset()
        chrono = pygame.time.Clock()
        sec = round(pygame.time.get_ticks() / 1000)

        loop = 1
        while loop:

            chrono.tick(60)
            fps = chrono.get_fps()
            # print(round(fps))

            # Chronometer_code
            if sec != round(pygame.time.get_ticks()/1000):
                sec = round(pygame.time.get_ticks()/1000)
                # print(sec//60,":", (sec//10)%6, sec%10)

            # screen.fill(white)
            game.blit_bg()
            game.blit_overlay()

            game.ia_turn(game)
            game.get_allinputs()
            game.apply_all_effects()
            game.complete_frame()

            game.stamina_restitution()

            loop = game.goal_verif2()

            game.blit_entities()
            game.blit_stadium()

            game.blit_playtags()

            game.blit_scores()
            game.blit_char_icon()
            game.blit_timer(sec)
            game.blit_stamina()
            game.blit_special()

            pygame.display.flip()







