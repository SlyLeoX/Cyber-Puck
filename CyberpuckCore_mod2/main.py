# Version 1.1a : Introduction des hitboxes rondes et de la var trucenter en remplacement des rect. (Version 1)
# Version 1.2a : Première introduction des controles au joystick + Fixs physiques divers, abandon de la var TrueCenter.
# 1.3a: Premiere versions des barres d'endurance, de spéciale, ajout du chronomètre et des premiers mouvements spéciaux.
# 1.4a: Intégration d'un overlay regroupant les informations de jeu.
# 1.5a: Implémentation du framework des Techniques spéciales.
# 1.6a: Début de travaux sur la refonte des inputs de jeu, optimisation des import calls, préparations au raccordement.
# 1.7a: Développement de la préintégration de l'IA dans les programmes du Core.


import pygame
from classOneGame import PartyOn
from Main_game import Main_game


if __name__ == '__main__':
    g = Main_game(1)
    g.display_menu()





