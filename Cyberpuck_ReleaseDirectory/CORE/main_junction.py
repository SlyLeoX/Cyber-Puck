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


def core(system_parameters, player_parameters, game_parameters, music="bensound-dance"):

    # Supercall synthax: (system_parameters, players_parameters, chosen_stadium)
    game = PartyOn(system_parameters, player_parameters, game_parameters[1])
    # We already extract the references to the player objects from the game object to examine some of their stats later.
    gp1, gp2 = game.players[0], game.players[1]

    # Joysticks initialization.
    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    # Background music initialization.
    # Currently fixated, a point of upgrade could be to offer the player the choice of the music.
    pygame.mixer.init()
    pygame.mixer.music.load(r'CORE\ressources\soundtracks\fix'.removesuffix("fix")+music+'.wav')
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play(-1)

    # init_date is used to compute the right current time later. Sec is here for plain initialization.
    init_date = pygame.time.get_ticks()
    sec = 0

    # The following lines decompose the type of game into the observed parameter and the required value.
    # Parameter may be like "time" or "points" and objective "120(s)" or "3(points)"
    parameter = (game_parameters[0].split("_"))[0]
    objective = int((game_parameters[0].split("_"))[1])

    # That variable is used by the "savage cut" to exit the match abruptly.
    condition = 1

    # Displays the match's victory requirements displayed before the match begins.
    game.begin_screen(parameter, objective)

    # Code for the countdown before the party engages. See in "auxiliary_Toolbox.py" to see the function text_screen.
    for j in range(3, -1, -1):
        text_screen(system_parameters, str(j), "white", 250)

    # The following while make it so the overall match continues as long as the selected objective is not fulfilled.
    while condition and ((gp1.score < objective and gp2.score < objective)if parameter == "score" else sec < objective):

        # We reset the entities parameters so they get back to their initial position after a point is scored.
        game.entities_reset()

        # Further initializations for the chronometer, sec is set to reflect the time since the beginning of the match.
        chrono = pygame.time.Clock()
        sec = round((pygame.time.get_ticks()-init_date) / 1000)

        # loop is used to make the actors reset when a goal is scored"
        loop = 1

        pause_asked = 0

        # The following while make it so the game continues as long as a goal is not scored or a quit is not asked.
        # It will also cut the match if the time limit (if any) is reached.
        while loop and ((gp1.score < objective and gp2.score < objective)if parameter == "score" else sec < objective):

            # The 2 following lines blocks the framerate at 60 seconds for a more uniform experience for weaker PCs.
            chrono.tick(60)
            fps = chrono.get_fps()

            # Chronometer_code
            if sec != round((pygame.time.get_ticks()-init_date) / 1000):
                sec = round((pygame.time.get_ticks()-init_date) / 1000)
                # print(sec//60,":", (sec//10)%6, sec%10)

            # Prints the first elements of the user Interface.
            game.blit_bg()
            game.blit_overlay()

            # Calls for a potential IA player to make its choices.
            game.ia_turn(game)

            # The following paragraph is the Commands system.
            command = game.get_allinputs()
            # If the players hits the F9 Key the game will cease all operation and go back to Menu (count as a defeat).
            if command == 0:
                loop = condition = 0
                break
            # If the player hits the Escape Key the game will PAUSE and display a Pause Message (later in the code).
            elif command == -1:
                pause_asked = 1

            # The game checks if it got 'effects' to apply/remove.
            game.apply_all_effects()

            # completer_frame is a subfunction that calls functions which make:
            # -Border Collisions Verification
            # -Colliding Physics Computation
            # -Actors displacement on the terrain according to their speed.
            game.complete_frame()

            # Call for the function that supplys a bit of energy to players each frame.
            game.stamina_restitution()

            # The game verifies if goal is scored, if so the loop ends and the actors will get reseted.
            loop = game.goal_verif2()

            # The game now Prints the actors and the remaining elements of the user Interface.
            game.blit_entities()
            game.blit_stadium()

            game.blit_playtags()

            game.blit_scores()
            game.blit_char_icon()
            game.blit_timer(sec)
            game.blit_stamina()
            game.blit_special()

            pygame.display.flip()

            # I put the Pause there in that way, because else parts of the game objects are invisible during pause.
            if pause_asked:
                pause_asked = 0
                game.pause_screen()

    # That condition make it so that regular end screen is only displayed if F9 has not been pressed.
    pygame.mixer.fadeout(5000)
    pygame.mixer.pause()
    if condition:
        # Ends the music
        # Prints the winner on the screen.
        winner = game.end_screen()

        return winner


# Junk reliquary bit of code, used to allow to launch a game before the unification of the programm.
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







