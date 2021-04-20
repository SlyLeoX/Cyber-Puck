from CORE.main_junction import core

def complete_campaign(system_parameters):

    # The player needs an intermediate menu before launching the campaign (choosing inputs and reading rules)
    # Currently actively wondering if I should use the same menu system as the future 'Pause' or ask Kevin.

    # For now there is only one planned campaign, so 1 'main' character only.

    levels_file = 'SOLO\levels.txt'
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

    for i in range(5):
        parameters = levels[i].split(",")
        print(parameters)
        player_parameters[1][0] = parameters[0]+"COM2"
        player_parameters[1][1] = parameters[1]
        game_parameters[0] = parameters[2]
        game_parameters[1] = parameters[3].removesuffix("\n")

        core(system_parameters, player_parameters, game_parameters, 300+i)