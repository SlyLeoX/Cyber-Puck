Eplications des dossiers :
-CyberpuckCore_mod2: The current architecture of the game's core. An object-programmed, multi-file nightmare containing every bit used to make the game run currently.
  -.jpg and .gif files remaining in the main folder are to be put in a proper ordonated folder.
  -main.py: The "arrival" file of the core, contains the primodial pygame initializations (for now) as well as the two main while loops (the match loop and the goal loop).
  -classOneGame.py: Contains the partyOn class mainly containing lists of elements on the field and most of the blits and secondary functions (linking functions from other files).
  -classMovable.py: Contains every variables common to every moving things as well as functions related to moving elements (physics, border verification and moving function)
  -classPlayer.py: Contains every variables exclusive to player-controlled objects (stamina, power)as well as functions exclusive to players (get and apply inputs)
  -classEffect.py: Contains variables belonging to powers used (dashes to ultra) as well as functions applying these powers. [CURRENTLY VERY WIP AND BUGGY]
  -classCom.py: Placeholder file that may contain the IA code later...
  -classMovableControlsAux.py: Contains an utilitary dictionnary containing current keyboard maps.
  -class Immuable.py: Contains variables related to immuable objects on field (essentially there is only the goals for now)

Changelog :
-CyberpuckCore_mod2 v1.5a (18.03 update) : adding the protype, proper interface as well as the prototype for the special moves class. (Joystick and songs absent)

Game is now in CyberpuckAlphaMergerd no.1
