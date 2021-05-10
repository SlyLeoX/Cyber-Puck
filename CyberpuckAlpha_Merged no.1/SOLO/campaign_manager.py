from CORE.main_junction import core
from CORE.auxiliary_Toolbox import text_screen, story_text_screen
from CORE.auxiliary_Stats import return_stadiumstats

from SOLO.chat_manager import chat

def complete_campaign(system_parameters):

    # The player needs an intermediate menu before launching the campaign (choosing inputs and reading rules)
    # Currently actively wondering if I should use the same menu system as the future 'Pause' or ask Kevin.

    # For now there is only one planned campaign, so 1 'main' character only.

    levels_file = r'SOLO\levels.txt'
    levels_file = open(levels_file, "r", encoding="UTF-8")
    levels = levels_file.readlines()

    # The idea right there would be to have the 2nd and 3rd set of parameters be loaded from a text file.
    # Number of levels: 5 (so same number of characters +1 ?)
    # Confirmed varying parameters: opponent character, ia_level, "win_condition", terrain_parameters.
    # Not confirmed parameters: number of opponents (widely unsupported as of the M3.1a).
    # Unvarying parameters: opponent's map is Null, is "COM2", "bumper" appearance is linked to the character.

    # Putting that there for initializing's sake.
    # The first half of player parameters (inputs i mean) shall be affected by players choice.
    player_parameters = [["PLAYER1", "Sanic", "keyboard1"],["0COM2", "Alexander", "0"]]
    game_parameters = ["first_to3", "metal1"]

    i = 0
    winner = 0

    # Counter intuitive but the core should return 0 if the player win (cause he's no.0 in the array of players)
    # Might correct that later
    while i < 5 and winner == 0:
        parameters = levels[i].split(",")
        print(parameters)
        player_parameters[1][0] = parameters[0]+"COM2"
        player_parameters[1][1] = parameters[1]
        game_parameters[0] = parameters[2]
        game_parameters[1] = parameters[3]

        prolog = parameters[4]
        epilog = parameters[5].removesuffix("\n")


        #This paragraph print the story in text mode.
        dialogue_file = (r"SOLO\stories\fix".removesuffix("fix")) + str(i+1) + ".txt"
        dialogue_file = open(dialogue_file, "r", encoding="UTF-8")
        dialogue = dialogue_file.readlines()
        story_text_screen(system_parameters,dialogue,"black",20)



        text_screen(system_parameters, "LEVEL 0"+str(i+1), "white", 5000)
        if int(prolog): chat(system_parameters, prolog, return_stadiumstats(game_parameters[1])[0])

        winner = core(system_parameters, player_parameters, game_parameters, 300+i)
        if int(epilog) and winner == 0 : chat(system_parameters, epilog, return_stadiumstats(game_parameters[1])[0])
        i += 1

    if i < 5 or winner != 0:
        text_screen(system_parameters, "GAME OVER", "red", 5000)
    else:
        dialogue_file = (r"SOLO\stories\fix".removesuffix("fix")) + str(6) + ".txt"
        dialogue_file = open(dialogue_file, "r", encoding="UTF-8")
        dialogue = dialogue_file.readlines()
        story_text_screen(system_parameters, dialogue, "black", 20)
        text_screen(system_parameters, "CONGRATULATIONS-YOU BEAT THE GAME", "green", 5000)
