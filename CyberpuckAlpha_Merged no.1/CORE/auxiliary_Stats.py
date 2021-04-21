

def return_charstats(character):

    if character=="0":
        return [5]

    elif character == 'Sanic':
        # Pattern: [mass,max_endurance,max_pow,icon,[ultra,special,passive]]
        return [10,25,12,r"CORE\ressources\characters\sanic\icon.png",[100*60,"ultra0,puck_speedup4"],[100*60,"super0,enemy_speeddown2"],[]]

    elif character == 'Alexander':
        return [20,20,12,r"CORE\ressources\characters\alexander\icon.png",[100*60,"Ultra0,puck_speedup2"],[100*60,"super0,enemy_speeddown4"],[]]


def return_stadiumstats(terrain):
    if terrain=="metal1":
        # Pattern: [terrain_texture, terrain roughness]
        return (r"CORE\ressources\game_bg\metal_1.jpg", 200)
