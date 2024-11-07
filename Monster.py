import random as r

def monster():
    monster_str = r.randint(5,15)
    player_hp = 100
    player_str = 10
    player_lvl = 0

    if player_str < monster_str:
        print("You lost the fight, you lost hp")
        player_hp -= 1
    elif monster_str < player_str:
        print("You beat the monster, your level increaced")
        player_lvl += 1
    elif player_str == monster_str:
        print("Nothing happend")
    else: 
        print("felmedelande")