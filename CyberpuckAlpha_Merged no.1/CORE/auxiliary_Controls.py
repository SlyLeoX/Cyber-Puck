import pygame


def controls_mapping(controller):

    if controller == "0":
        return {"up": 0, "down": 0, "left": 0, "right": 0, "spe_move": 0, "sup_move": 0, "ultra": 0}

    if controller == "keyboard1":
        return {"up": pygame.K_z, "down": pygame.K_s, "left": pygame.K_q, "right": pygame.K_d, "spe_move": pygame.K_h, "spe_move2": 2, "sup_move": pygame.K_j, "sup_move2": 3, "ultra": pygame.K_k, "ultra2": 1}

    if controller == "keyboard2":
        return {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "spe_move": pygame.K_KP1, "spe_move2": 2, "sup_move": pygame.K_KP2, "sup_move2": 3, "ultra": pygame.K_KP3, "ultra2": 1}

