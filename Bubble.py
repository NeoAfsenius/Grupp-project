import random as r
import sys
import time

class Spelare:
    def __init__(self, player_hp,player_str,player_luck, player_level):
        self.hp = player_hp
        self.str = player_str
        self.luck = player_luck
        self.level = player_level
        self.inventory = []
        # self.name = player_name

    def player_stats(self):
        print(f"HP: {self.hp}, STRENGTH: {self.str}, LUCK: {self.luck}, LEVEL: {self.level}")
        Alternative()
  
    def add_to_inventory(self, item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
            print(f"Du la till {item} i ditt inventory")
            print("")
            Alternative()
        else:
            print("Ditt inventory är fullt, ta bort ett item för att lägga till det nya")
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
        print(self.inventory) 
        print("")
        Alternative()

class Item:
    def __init__(self, strength_bonus, health_bonus, luck_bonus):
        self.str_bonus = strength_bonus
        self.hp_bonus = health_bonus
        self.luck_bonus = luck_bonus

def create_sword():
    return Item(2,2,0)

def create_belt():
    return Item(0,5,0)

def create_potion():
    return Item(15,0,0,)

def create_luckybraclet():
    return Item(0,0,2)

def create_unluckyboots():
    return Item(0,-10,0)


name = input("Spelarens namn: ") 
name = Spelare(100, 10, 1, 1)
room_count = 0



def print_with_delay(text, delay=0.01):
    # Skriver text med fördröjning
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        #Gå tillbaka till meny

def Room_monster():
    print("Du öppnar dörren, och ser ett monster.\n ")
    Monster_Action = input("Vill du fly(1) eller attakera(2)? ")
    # try:
    if Monster_Action == "1":
            Escape_monster()

    elif Monster_Action == "2":
            Fight_monster()
    # except:
    #     print("Error, try again")

def Fight_monster():
    monster_damage = r.randint(1+(3*name.level), 10+(3*name.level))
    if monster_damage >= name.str:
        name.hp = name.hp-2*monster_damage
        print("Du förlorade och tog skada")
        print(f"Du har nu {name.hp} Hp")
        print("")
        Alternative()
    elif monster_damage == name.str:
        print("Ni är lika starka, du går vidare")
        Alternative()
    if monster_damage <= name.strr:
        name.level =+ 1
        name.str=+ 2
        lucky_number = r.randint(1,7)
        
        if lucky_number%7==0:

            name.luck=+ 1
            print("Du har tur och fick även +1 luck när du levlade upp!")
        Alternative()

def Escape_monster():
    tempo_luck = name.luck
    if name.luck >= 9:
        name.luck = 9
    Escape_chance = r.randint(0+(name.luck),10)
    name.luck = tempo_luck
    escape_damage = r.randint(1+(3*name.level), 10+(3*name.level))

    print("Du försöker fly")
    if Escape_chance >= 5:
        print("Du lyckades att fly från monstret ")
        Alternative()
    elif Escape_chance < 5:
        print("Du lyckades inte att fly från monstret och därför tog du skada")
        escape_damage = r.randint(10 , 20-(name.luck))
        name.hp=name.hp - escape_damage
        print("Du tog " + str(escape_damage) + " Skada")
        print("Du har nu " + str(name.hp) +  "HP")
        Alternative()

def Room_chest():
    print("Du öppnar dörren, och ser en kista.\n ")

    #Nödvädnigt med try?
    if name.luck == 1:
        chest_chance = r.randint(1, 20)
    elif name.luck == 2: 
        chest_chance = r.randint(1+2*name.luck, 20)
    if chest_chance >5 and chest_chance <21:
        if chest_chance >5 and  chest_chance<9:
            sword = create_sword()
            name.add_to_inventory(sword)
        elif chest_chance >=9 and  chest_chance<12:
            luckybraclet = create_luckybraclet()
            name.add_to_inventory(luckybraclet)
        elif chest_chance >=12 and chest_chance<17:
            belt = create_belt()
            name.add_to_inventory(belt)
        elif chest_chance >=17 and chest_chance<21:
            potion = create_potion()
            name.add_to_inventory(potion)
    elif chest_chance <=5:
        unluckyboots = create_unluckyboots()
        name.add_to_inventory(unluckyboots)

def Room_trap():
    print("Du öppnar dörren, och blir tagen i en fälla.\n ")
    damage = r.randint(10,40)/name.luck
    name.hp =- damage
    print(f"Du tog {damage} i skada")
    Alternative()

# ALTERNATIV 
def Alternative():
    print(" [1] - Välj mellan 3 dörrar. \n [2] - Öppna inventory. \n [3] - Meny. \n [4] - Se Stats \n ")

    try:
        Answer = int(input("Ange vad du vill göra nu: "))
        if Answer == 1:
            Valt_rum()
        elif Answer == 2:
            name.show_inventory()
        elif Answer == 3:
            Menu()
        elif Answer == 4:
            name.player_stats()
        elif Answer < 1 or Answer > 4:
            print("\n Fel! Ange ett giltigt tal 1-4")
            Alternative()
    except ValueError:
        print("\n Fel! Ange ett giltigt tal 1-4")
        Alternative()

# MENYN
def Menu():
    MenuLoop = 1
    while MenuLoop != 3:
        print("\n [1] - Återuppta spelet \n [2] - Avsluta spelet")
        
        try:
            MenuAnswer = int(input("Ange ditt val här: "))
            if MenuAnswer == 1:
                print("Återupptar spelet..")
                print(" ")
                MenuLoop = MenuLoop + 2
                Alternative()
            elif MenuAnswer == 2:
                print("Avslutar spelet..")
                break 
            else:
                print(" ")
                print("Ogiltigt val. Ange 1 eller 2")
        except ValueError:
            print(" ")
            print("Fel! Ange ett giltigt tal 1-2")


def Valt_rum():
    g = int(input("""
Välj dörr
Dörr 1:
Dörr 2:
Dörr 3:
"""))
    try:
        random_tal=r.randint(1,3)
        if random_tal == 1:
            Room_monster()
        elif random_tal == 2:
            Room_trap()
        elif random_tal == 3:
            Room_chest()  
        elif random_tal < 1 or random_tal > 3:
            print("\n Fel! Ange ett tal mellan 1-3")
            Valt_rum()
    except ValueError:
        print("\n Fel! Ange ett tal mellan 1-3")

def game_intro():
    #Skriver backstory
    intro_text = f"""
Välkommen till spelet, {name}!
Du kommer få välja mellan att öppna dörrar som kan innehålla monster, fällor,
eller kistor med loot som hjälper dig att gå vidare.
"""

    print_with_delay(intro_text)
    Alternative()

game_intro()