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

import pygame
from CORE.classOneGame import PartyOn

white = 255, 255, 255
black = 0, 0, 0
red = 255, 65, 65
blue = 65, 65, 255

def core(system_parameters,player_parameters,game_parameters):
    # Supercall synthax: (system_parameters, players_parameters, chosen_stadium)
    game = PartyOn(system_parameters, player_parameters, game_parameters[1])
    gp1, gp2 = game.players[0], game.players[1]
    sec = 0

    # Joysticks initialization.
    pygame.joystick.init()
    joystick = []
    for i in range(pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[-1].init()

    # Victoryloops condition.
    condition = 1
    #if game_parameters[0] == "first_to3":
        #condition = gp1.score < 3 and gp2.score < 3
    #elif game_parameters[0] == "time_to120" or 1:
        #condition = sec < 121

    pygame.mixer.init()
    pygame.mixer.music.load(r'CORE\ressources\soundtracks\UNL Pre-Battle Theme - The Legendary Titan.wav')
    pygame.mixer.music.queue(r'CORE\ressources\soundtracks\UNL Pre-Battle Theme - Our Hisou Tensoku.wav')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    init_date=pygame.time.get_ticks()

    while condition and (gp1.score < 3 and gp2.score < 3 if game_parameters[0] == "first_to3" else  sec < 121):

        game.entities_reset()
        chrono = pygame.time.Clock()
        sec = round((pygame.time.get_ticks()-init_date) / 1000)

        loop = 1
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
            #Superbreak
            if command == 0:
                loop = condition = 0
                break
            #Pause
            elif command == -1:
                game.pause_screen()

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

    if condition:
        #MAKE A FUNCTION OUT OF THESE LATER
        if game.players[0].score > game.players[1].score:
            winner = 0
        elif game.players[1].score > game.players[0].score:
            winner = 1
        else:
            winner = -1
        misc_text = pygame.font.SysFont('Calibri', 30)
        if winner < 0:
            winner = misc_text.render("PAR !", False, red)
        else:
            winner = misc_text.render(player_parameters[winner][1]+" WINS!", False, red)
        system_parameters[0].blit(winner,((system_parameters[1][0]/2),(system_parameters[1][1]/2)))
        pygame.display.flip()

        pygame.time.delay(5000)
        pygame.mixer.fadeout(5)


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
    player_parameters = [["PLAYER1", "Sanic", "keyboard1", r"ressources\misc\player_bumper.gif"],
                         ["COM2", "Alexander", "keyboard2", r"ressources\misc\player_bumper.gif"]]
    # Synthax: [gametype, terrain chosen]
    game_parameters = ["first_to3", "metal1"]


    core(system_parameters,player_parameters,game_parameters)







