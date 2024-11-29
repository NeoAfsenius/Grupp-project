import random as r
import sys
import time

class Spelare:
    def __init__(self, player_hp,player_str,player_luck, player_level, player_name):
        self.hp = player_hp
        self.str = player_str
        self.luck = player_luck
        self.level = player_level
        self.inventory = []
        self.name = player_name

    def player_stats(self):
        print(f"\n \n \n \n HP: {self.hp}, STRENGTH: {self.str}, LUCK: {self.luck}, LEVEL: {self.level}")
  
    def add_to_inventory(self, item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
            print(f"Du la till {item} i ditt inventory")

            self.str += item.str_bonus
            self.hp += item.hp_bonus
            self.luck += item.luck_bonus

            print("")
            
            Alternative()
        else:
            inventory_full()

            print("")
            Alternative()

    def remove_from_inventory(self, item):
        if len(self.inventory) <= 5:
            self.inventory.remove(item)
            print(f"Tog bort {item}ur inventoryt")
            print("")
            Alternative()
        elif len(self.inventory) == 0: 
            print("Finns inga nuvarande items i ditt inventory")
            print("")
            Alternative()

    def show_inventory(self):
        for item in self.inventory:
            print(item)
        print("")
        Alternative()

class Item:
    def __init__(self, strength_bonus, health_bonus, luck_bonus, namn):
        self.str_bonus = strength_bonus
        self.hp_bonus = health_bonus
        self.luck_bonus = luck_bonus
        self.name = namn

    #Gör så att itemnamnet kan läsas av,
    def __str__(self):
        return f"{self.name} (STR: {self.str_bonus}, HP: {self.hp_bonus}, LUCK: {self.luck_bonus})"
def create_sword():
    return Item(r.randint(1,10),r.randint(1,10),0,"sword")

def create_belt():
    return Item(0,5,0, "belt")

def create_potion():
    return Item(15,0,0, "potion")

def create_luckybraclet():
    return Item(0,0,2, "braclet")

def create_unluckyboots():
    return Item(0,0,0, "boots")


player = input("Spelarens namn: ") 
print(" ")
player = Spelare(100, 10, 1, 1, player)
room_count = 0

def inventory_full():
    inventory_remove_check = input("Ditt inventory är fullt, ta bort ett item för att lägga till det nya\n [1] - Ta bort ett item \n[2] - Gå vidare")
    if inventory_remove_check == "1":
        chosen_removal = input("Vilket nummer på item vill du ta bort")
        player.remove_from_inventory(player.inventory[chosen_removal-1])
    elif inventory_remove_check == "2":
        Alternative()
    elif inventory_remove_check != "1" or inventory_remove_check != "2":
        print("Error, skriv in 1 eller 2")

    

def print_with_delay(text, delay=0.01):
    # Skriver text med fördröjning
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        #Gå tillbaka till meny

def Room_monster():
    monster_text = f"""
Du öppnar dörren, och ser ett monster
Vill du fly[1] eller attackera[2]
"""
    print_with_delay(monster_text)
    Monster_Action = input("")
    # try:
    if Monster_Action == "1":
        Escape_monster()
    elif Monster_Action == "2":
        Fight_monster()
    elif Monster_Action != "1" or  Monster_Action != "2":
        print("\n\n\n\n")
        print("Error, Du måste skriva 1 eller 2")
        Room_monster()
        

    # except:
    #     print("Error, try again")

def Fight_monster():
    monster_hp = r.randint(50+(5*player.level), 100+(5*player.level))
    monster_choice=int(input("""
       ____  ____
     /          o  
    |   ( )   ( )   | 
    |      >  <      |   _  _    <--- Rargh!!
    |    \_____/    |  / \/ 
     \__________/   /_/      
        /       \      (___|_)
      /          \    |   |   |
     |            |   |___|___|
     |____________|
      |   ||  ||   |
      |   ||  ||   |
      |_||_|  |_||_|

          

Du möter ett monster!
Vad vill du göra
[1] En lätt attack [2] En tung attack [3] Försöka undvika hans attack
->
"""))
    if monster_choice == 1:
        light_attack = r.randint(20+(player.str),30+(player.str))
        print(f"""
Du gör en lätt attack på honom och skadar honom 
""")
        monster_hp = monster_hp-light_attack
    elif monster_choice ==2:
        heavy_attack = r.randint(40+(player.str),50+(player.str))
        attack_chance=r.random(1,5)
        if attack_chance==5:
            print("Du slår hårt men missar! ")
        elif attack_chance<5:
            print(f"""
Du slår hårt och och träffar.
Du gör {heavy_attack} damage på monstret
""")
            monster_hp=monster_hp-heavy_attack
    elif monster_choice == 3:
        dodge_chance=r.random(1,5)
        if dodge_chance==5:
            monster_damage = r.randint(1+(2*player.level), 10+(2*player.level))
            print(f"""
Du försöker undvika men du blir träffad och tar {monster_choice} damage
""")
        elif dodge_chance<=5:
            print(f"""
Du undviker honom och får ett till försök
""")

    # if monster_damage >= player.str:
    #     player.hp = player.hp-2*monster_damage
    #     print("Du förlorade och tog skada")
    #     print(f"Du har nu {player.hp} Hp")
    #     print("")
    #     Alternative()
    # elif monster_damage == player.str:
    #     print("Ni är lika starka, du går vidare")
    #     Alternative()
    # if monster_damage <= player.str:
    #     player.level = player.level + 1
    #     player.str= player.str + 2
    #     lucky_number = r.randint(1,7)
    #     print("Du vann över monstret och gick upp i Level och din str gick upp 2 enheter")
    #     if lucky_number%7==0:
    #         player.luck=+ 1
    #         print("Du har tur och fick även +1 luck när du levlade upp!")
    #     Alternative()

def Escape_monster():
    tempo_luck = player.luck
    if player.luck >= 9:
        player.luck = 9
    Escape_chance = r.randint(0+(player.luck),10)
    player.luck = tempo_luck
    escape_damage = r.randint(1+(3*player.level), 10+(3*player.level))

    if Escape_chance >= 5:
        escape_text=(f"""
Du smyger runt dörren och lyckas att inte bli sedd!
Men du är nu tillbaka i ett rum som ser likadant ut!
""")
        print_with_delay(escape_text)
        Alternative()
    elif Escape_chance < 5:
        failescape_text=("""
Du försöker smyga runt hörnet men monstret hittat dig och skadar dig!
""")
        print_with_delay(failescape_text)
        escape_damage = r.randint(10 , 20-(player.luck))
        player.hp=player.hp - escape_damage
        dmg_taken=f"""
Du tog {escape_damage} Skada
"""
        print_with_delay(dmg_taken)
        dmg_left=(f"""
Du har nu {player.hp} hp
""")
        print_with_delay(dmg_left)
        Alternative()

def Room_chest():
    print("Du öppnar dörren, och ser en kista.\n ")

    #Nödvädnigt med try?
    # Bestäm chansen baserat på spelarens tur
    if player.luck == 1:
        chest_chance = r.randint(1, 20)
    elif player.luck >= 2: 
        chest_chance = r.randint(1 + 2 * player.luck, 20)
    elif player.luck < 1:
        chest_chance = r.randint(1, 20)
    


    if chest_chance >5 and chest_chance <21:
        if chest_chance >5 and  chest_chance<9:
            sword = create_sword()
            player.add_to_inventory(sword)
        elif chest_chance >=9 and  chest_chance<12:
            luckybraclet = create_luckybraclet()
            player.add_to_inventory(luckybraclet)
        elif chest_chance >=12 and chest_chance<17:
            belt = create_belt()
            player.add_to_inventory(belt)
        elif chest_chance >=17 and chest_chance<21:
            potion = create_potion()
            player.add_to_inventory(potion)
    elif chest_chance <=5:
        unluckyboots = create_unluckyboots()
        player.add_to_inventory(unluckyboots)

def Room_trap():
    print("Du öppnar dörren, och blir tagen i en fälla.\n ")
    damage = r.randint(5,20)/player.luck
    player.hp -= damage
    print(f"Du tog {damage} i skada")
    print(f"Du har nu {player.hp} hp kvar!")
    Alternative()

# ALTERNATIV 
def Alternative():
    if player.hp > 0:
        player.player_stats()
        print(" \n [1] - Välj mellan 3 dörrar \n [2] - Öppna inventory \n [3] - Meny \n ")
        try:
            Answer = int(input("Ange vad du vill göra nu: "))
            if Answer == 1:
                Valt_rum()
            elif Answer == 2:
                player.show_inventory()
            elif Answer == 3:
                Menu()
            elif Answer < 1 or Answer > 3:
                print("\n Fel! Ange ett giltigt tal 1-3")
                Alternative()
        except ValueError:
            print("\n Fel! Ange ett giltigt tal 1-4")
            Alternative()
    if player.hp <= 0: 
        print("Du förlorade!")

# MENYN
def Menu():
    MenuLoop = 1
    while MenuLoop != 3:
        print("\n \n \n \n \n \n \n [1] - Återuppta spelet \n [2] - Avsluta spelet \n ")
        
        try:
            MenuAnswer = int(input("Ange ditt val här: "))
            if MenuAnswer == 1:
                print("\n \n \n \n Återupptar spelet..")
                print(" ")
                MenuLoop = MenuLoop + 2
                Alternative()
            elif MenuAnswer == 2:
                print("\nAvslutar spelet..\n")
                break 
            else:
                print(" ")
                print("Ogiltigt val. Ange 1 eller 2")
        except ValueError:
            print(" ")
            print("Fel! Ange ett giltigt tal 1-2")


def Valt_rum():
    try:
        g = int(input("""
\n \n \n \n \n
Välj vilken dörr du vill öppna.
[1] - Blå dörr
[2] - Röd dörr
[3] - Grön dörr

Ange dörr: """))
        # Kontrollera om input är inom rätt intervall
        if g < 1 or g > 3:
            print("\nFel! Ange ett tal mellan 1-3")
            Valt_rum()  # Anropa funktionen igen
        else:
            # Generera ett slumpmässigt rum
            random_tal = r.randint(1, 3)
            if random_tal == 1:
                Room_monster()
            elif random_tal == 2:
                Room_trap()
            elif random_tal == 3:
                Room_chest()
    except ValueError:
        print("\nFel! Ange ett giltigt tal 1-3")
        Valt_rum()  


def game_intro():
    #Skriver backstory
    intro_text = f"""
Välkommen till spelet, {player.name}!
Du kommer få välja mellan att öppna dörrar som kan innehålla monster, fällor,
eller kistor med loot som hjälper dig att gå vidare.

"""

    print_with_delay(intro_text)
    starta = int(input("Vill starta spelet \n [1] - Ja \n [2] - Nej \n \n Ange ditt val: "))
    if starta == 1: 
        Alternative()
    elif starta == 2:
        print("hejdå")

game_intro()