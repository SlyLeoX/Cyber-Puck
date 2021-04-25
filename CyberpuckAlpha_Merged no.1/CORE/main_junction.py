# Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)
# Version 1.2a : Première introduction des controles au joystick + Fixs physiques divers, abandon de la var TrueCenter.
# 1.3a: Premiere versions des barres d'endurance, de spéciale, ajout du chronomètre et des premiers mouvements spéciaux.
# 1.4a: Intégration d'un overlay regroupant les informations de jeu.
# 1.5a: Implémentation du framework des Techniques spéciales.
# 1.6a: Début de travaux sur la refonte des inputs de jeu, optimisation des import calls, préparations au raccordement.
# 1.7a: Développement de la préintégration de l'IA dans les programmes du Core.
# 1.8a: Intégration des Musiques et Sons
# 1.9a: Intégration de l'IA v1.

# M3.Oa: Merging done + Begins on Begin and End Screens + Legacy GetInputs"1" got deleted
# M3.1a: Intégration de la commande de sortie de jeu "sauvage". (F9)
# M3.2a: Intégration du système de base du mode Solo.

import pygame
from CORE.classOneGame import PartyOn
from CORE.auxiliary_Toolbox import text_screen

white = 255, 255, 255
black = 0, 0, 0
red = 255, 65, 65
blue = 65, 65, 255


def core(system_parameters, player_parameters, game_parameters, dialogues_avaiable=99):
    # Supercall synthax: (system_parameters, players_parameters, chosen_stadium)
    game = PartyOn(system_parameters, player_parameters, game_parameters[1])
    gp1, gp2 = game.players[0], game.players[1]

    # Joysticks initialization.
    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    # Background music initialization.
    pygame.mixer.init()
    pygame.mixer.music.load(r'CORE\ressources\soundtracks\UNL Pre-Battle Theme - The Legendary Titan.wav')
    pygame.mixer.music.queue(r'CORE\ressources\soundtracks\UNL Pre-Battle Theme - Our Hisou Tensoku.wav')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    # init_date is used to compute the right current time later. Sec is here for plain initialization.
    init_date=pygame.time.get_ticks()
    sec = 0

    print(type(gp1))
    print(type(gp2))

    # The following lines decompose the type of game into the observed parameter and the required value.
    parameter = (game_parameters[0].split("_"))[0]
    objective = int((game_parameters[0].split("_"))[1])

    # That variable is used by the "savage cut" to exit the match abruptly.
    condition = 1

    # Displays the match's victory requirements.
    game.begin_screen(parameter,objective)

    # Code for the countdown before the party engages
    for j in range(3, -1, -1):
        text_screen(system_parameters, str(j), "white", 250)

    while condition and ((gp1.score < objective and gp2.score < objective)if parameter == "score" else sec < objective):

        game.entities_reset()
        chrono = pygame.time.Clock()
        sec = round((pygame.time.get_ticks()-init_date) / 1000)

        loop = 1
        pause_asked = 0
        while loop and (gp1.score < 3 and gp2.score < 3 if game_parameters[0] == "first_to3" else sec < 120):

            chrono.tick(60)
            fps = chrono.get_fps()
            # print(round(fps))

            # Chronometer_code
            if sec != round((pygame.time.get_ticks()-init_date) / 1000):
                sec = round((pygame.time.get_ticks()-init_date) / 1000)
                # print(sec//60,":", (sec//10)%6, sec%10)

            # screen.fill(white)
            game.blit_bg()
            game.blit_overlay()

            game.ia_turn(game)

            # The following pragraph is the embryo for the PAUSE system. Currently not working.
            command = game.get_allinputs()
            # Superbreak
            if command == 0:
                loop = condition = 0
                break
            # Pause
            elif command == -1:
                pause_asked = 1

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

            # I put that there in that way, because else parts of the game objects are invisible during pause.
            if pause_asked:
                pause_asked = 0
                game.pause_screen()

    # That condition make it so that regular end screen is only displayed if F9 has not been pressed.
    if condition:
        pygame.mixer.fadeout(5000)
        winner = game.end_screen()


        return winner


if __name__ == '__main__':

    # The following three lines will have to be erased when
    pygame.init()
    size = width, height = 1366, 768
    screen = pygame.display.set_mode(size)

    # The following lines contains values that will have to be given as a parameter when calling the core.
    # Synthax: [screen,[window_width, window_height]]
    system_parameters = [screen, [width, height]]
    # Synthax for each: [Player_type(player or IA)+ID,Chosen_Character,Chosen_Peripheral,Chosen_Bumber_Texture]
    # Also called infopacks later in the code
    player_parameters = [["PLAYER1", "Sanic", "keyboard1"],
                         ["0COM2", "Alexander", "keyboard2"]]
    # Synthax: [gametype, terrain chosen]
    game_parameters = ["score_3", "metal1"]


    core(system_parameters,player_parameters,game_parameters)







