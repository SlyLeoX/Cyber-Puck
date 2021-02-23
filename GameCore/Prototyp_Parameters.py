import pygame


def controls_mapping(controller):

    if controller == "0":
        return 0

    if controller == "keyboard1":
        return {"up": pygame.K_z, "down": pygame.K_s, "left": pygame.K_q, "right":pygame.K_d}

    if controller == "keyboard2":
        return {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}

    #Um, and I'm not doing the joystick/gamepad part, check the wiki, you'll understand X-X