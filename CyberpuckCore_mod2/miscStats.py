

def return_charstats(character):

    if character=="0":
        return [5]

    elif character == 'Sanic':
        #Pattern: [mass,max_endurance,max_pow,icon,[ultra,special,passive]]
        return([10,25,12,"char_icons\sanic_icon.gif",[100*60,"ultra0,puck_speedup4"],[100*60,"super0,enemy_speeddown2"],[]])



def return_stadiumstats(terrain):
    if terrain=="metal1":
        #Pattern: [terrain_texture, terrain roughness]
        return ("metal_bg.jpg", 200)
