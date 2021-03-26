import pygame


def controls_mapping(controller):

    if controller == "0":
        return 0

    if controller == "keyboard1":
        return {"up": pygame.K_z, "down": pygame.K_s, "left": pygame.K_q, "right":pygame.K_d, "spe_move":pygame.K_h, "sup_move":pygame.K_j, "ultra":pygame.K_k}

    if controller == "keyboard2":
        return {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "spe_move":pygame.K_KP1, "sup_move":pygame.K_KP2, "ultra":pygame.K_KP3}
