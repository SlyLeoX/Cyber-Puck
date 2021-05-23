from CORE.main_junction import core
from CORE.auxiliary_Toolbox import text_screen, story_text_screen
from CORE.auxiliary_Stats import return_stadiumstats

from SOLO.chat_manager import chat

def complete_campaign(system_parameters):

    # For now there is only one planned campaign, so 1 'main' character only.

    # We read the file containing the parameter of each match of the story mode.
    levels_file = r'SOLO\levels.txt'
    levels_file = open(levels_file, "r", encoding="UTF-8")
    levels = levels_file.readlines()

    # The idea right there would be to have the 2nd and 3rd set of parameters be loaded from a text file.
    # Number of levels: 5
    # Confirmed varying parameters: opponent character, ia_level, "win_condition", terrain_parameters.
    # Unvarying parameters: opponent's map is Null, is "COM2".

    # Putting that there for initializing sake.
    player_parameters = [["PLAYER1", "Alexander", "keyboard1"],["0COM2", "Alexander", "0"]]
    game_parameters = ["first_to3", "metal1"]

    i = 0
    winner = 0

    # Counter intuitive but the core should return 0 if the player win (cause he's no.0 in the array of players)
    # Might correct that later
    # If the player lose a match, we exit the while and get a game over screen.
    while i < 5 and winner == 0:
        # We get the right parameters from the read file;
        parameters = levels[i].split(",")
        #print(parameters)
        player_parameters[1][0] = parameters[0]+"COM2"
        player_parameters[1][1] = parameters[1]
        # Match objectives
        game_parameters[0] = parameters[2]
        # Terrain parameters
        game_parameters[1] = parameters[3]

        # Storing the path to the file containing fast dialogues before the match begins.
        prolog = parameters[4]
        epilog = parameters[5]

        chat_bg = r"CORE\ressources\game_bg\fix".removesuffix("fix")+parameters[6]+".jpg"

        music = parameters[7].removesuffix("\n")

        # This paragraph print the story in text mode.
        dialogue_file = (r"SOLO\stories\fix".removesuffix("fix")) + str(i+1) + ".txt"
        dialogue_file = open(dialogue_file, "r", encoding="UTF-8")
        dialogue = dialogue_file.readlines()
        story_text_screen(system_parameters,dialogue,"black",20)

        # This prints the number of the level before the match begins.
        text_screen(system_parameters, "LEVEL 0"+str(i+1), "white", 5000)

        # Launch a small dialogue before the match if avaiable.
        if int(prolog): chat(system_parameters, prolog, chat_bg)

        winner = core(system_parameters, player_parameters, game_parameters, music)

        # Launch a small dialogue after the match if avaiable, if the player won.
        if int(epilog) and winner == 0 : chat(system_parameters, epilog, chat_bg)
        i += 1

    # Case the player got out of the while before the last level:
    if i < 5 or winner != 0:
        text_screen(system_parameters, "GAME OVER", "red", 5000)
    # Case the player won the last match:
    else:
        dialogue_file = (r"SOLO\stories\fix".removesuffix("fix")) + str(6) + ".txt"
        dialogue_file = open(dialogue_file, "r", encoding="UTF-8")
        dialogue = dialogue_file.readlines()
        story_text_screen(system_parameters, dialogue, "black", 20)
        text_screen(system_parameters, "CONGRATULATIONS-YOU BEAT THE GAME", "green", 5000)
