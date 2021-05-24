
# Contains the statistics of the characters as arrays.
# It includes mass, max energy and techniques points, path to their portrait and description of their techniques.
# There is a 0 character stat that is used for objects that are not players: so the puck.
def return_charstats(character):

    if character == "0":
        return [5]

    elif character == 'Sanic':
        # Pattern: [mass,max_endurance,max_pow,icon,[ultra,special,passive]]
        return [10, 25, 12, r"CORE\ressources\characters\sanic\icon.png", [100*60, "super0,puck_speedup3"], [100*60, "ultra0,enemy_speeddown2"], []]

    elif character == 'Alexander':
        return [20, 20, 12, r"CORE\ressources\characters\alexander\icon.png", [100*60, "super0,puck_speedup2"], [100*60, "ultra0,gdmp0"], []]

    elif character == 'Harry':
        return [20, 15, 12, r"CORE\ressources\characters\harry\icon.png", [100*60, "super0,puck_speedup2"], [100*60, "ultra0,gdmp0"], []]

    elif character == 'Remilia':
        return [15, 20, 8, r"CORE\ressources\characters\remilia\icon.png", [100 * 60, "super0,puck_speedup2"],[100 * 60, "ultra0,gdmp0"], []]

    elif character == 'Sakuya':
        return [15, 30, 12, r"CORE\ressources\characters\sakuya\icon.png", [50 * 60, "super0,puck_speedup3"], [50 * 60, "ultra0,enemy_speeddown2"], []]

    elif character == 'King':
        return [35, 20, 12, r"CORE\ressources\characters\king\icon.png", [100 * 60, "super0,puck_speedup2"], [100 * 60, "ultra0,gdmp0"], []]


# Contains the statistics of the terrains as arrays.
# It path to the image and friction index.
def return_stadiumstats(terrain):
    if terrain=="metal1":
        # Pattern: [terrain_texture, terrain roughness]
        return (r"CORE\ressources\game_bg\metal_1.jpg", 200)
    if terrain=="stone1":
        return (r"CORE\ressources\game_bg\stone_1.jpg", 100)
    else:
        return (r"CORE\ressources\game_bg\wood_1.jpg", 50)
