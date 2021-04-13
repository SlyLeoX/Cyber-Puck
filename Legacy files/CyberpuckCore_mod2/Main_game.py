import pygame
from CyberpuckCore_mod2.classOneGame import PartyOn
from CyberPuck3.Application import Application

class Main_game(Application):
    def __init__(self, game):
        #Application.__init__(self, game)
        pass

    def display_menu(self):
        # The following three lines will have to be erased when
        pygame.init()
        size = width, height = 1366, 768
        screen = pygame.display.set_mode(size)

        # The following lines contains values that will have to be given as a parameter when calling the core.
        # Synthax: [screen,[window_width, window_height]]
        system_parameters = [screen, [width, height]]
        # Synthax for each: [Player_type(player or IA)+ID,Chosen_Character,Chosen_Peripheral,Chosen_Bumber_Texture]
        # Also called infopacks later in the code
        player_parameters = [["PLAYER1", "Sanic", "keyboard1", r"..\CyberPuckCore_mod2\ressources\misc\player_bumper.gif"],
                             ["COM2", "Alexander", "keyboard2", r"..\CyberPuckCore_mod2\ressources\misc\player_bumper.gif"]]
        # Synthax: [gametype, terrain chosen]
        game_parameters = ["first_to3", "metal1"]

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
        condition = 0
        if game_parameters[0] == "first_to3":
            condition = gp1.score < 3 and gp2.score < 3
        elif game_parameters[0] == "time_to3":
            condition = sec <= 180

        pygame.mixer.init()
        pygame.mixer.music.load(r'..\CyberPuckCore_mod2\ressources\soundtracks\UNL Pre-Battle Theme - The Legendary Titan.wav')
        pygame.mixer.music.queue(r'..\CyberPuckCore_mod2\ressources\soundtracks\UNL Pre-Battle Theme - Our Hisou Tensoku.wav')
        pygame.mixer.music.set_volume(0.05)
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
                if sec != round(pygame.time.get_ticks() / 1000):
                    sec = round(pygame.time.get_ticks() / 1000)
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

