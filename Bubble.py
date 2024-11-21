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
  

    def add_to_inventory(self, item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
            print(f"Du la till {item} i ditt inventory")
        else:
            print("Ditt inventory är fullt, ta bort ett item för att lägga till det nya")
    
    def remove_from_inventory(self, item):
        if len(self.inventory) <= 5:
            self.inventory.remove(item)
            print(f"Tog bort {item}ur inventoryt")
        elif len(self.inventory) == 0: 
            print("Finns inga nuvarande items i ditt inventory")

    def show_inventory(self, item):
        print(self.inventory) 

class Item:
    def __init__(self, strength_bonus, health_bonus, luck_bonus):
        self.str_bonus = strength_bonus
        self.hp_bonus = health_bonus
        self.luck_bonus = luck_bonus

    def sword(self, player):
        sword = Item(2,2,0,"Svärd")

        player.add_to_inventory(sword)
        print(f"Ett svärd hamnade i ditt inventory")

    def belt(self, player):
        belt = Item(0,5,0,"Bälte")

        player.add_to_inventory(belt)
        print(f"Ett svärd hamnade i ditt inventory")

    def potion(self, player):
        potion = Item(15,0,0,"Potion")

        player.add_to_inventory(potion)
        print(f"Ett svärd hamnade i ditt inventory")
    


name = input("Spelarens namn: ") 
name = Spelare(100, 10, 1, 1)

item = Item(2,2,2)

room_count = 0
chest = []

def print_with_delay(text, delay=0.005):
    # Skriver text med fördröjning
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        #Gå tillbaka till meny
def Valt_rum():
    g = int(input("""
Välj dörr
Dörr 1:
Dörr 2:
Dörr 3:
"""))
    # random_tal=r.randint(1,3)
    # print(random_tal)
    random_tal=1
    if random_tal == 1 :
        Room_monster()
    # if random_tal == 2 :
    #     Room_trap()
    # if random_tal == 3:
    #     Room_chest()

    
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
        name.hp=name.hp-2*monster_damage
        print("Du förlorade och tog skada")
        print("Du har nu" + str(name.hp) + " Hp")
        Alternative()
    else:
        name.level=name.level+1
        name.str=name.str+2
        lucky_number = r.randint(1,7)
        if lucky_number%7==0:
            name.luck=name.luck+1
        if name.level%5==0:
            hp = 100
        print("Du har vunnit och gått upp 1 level och 2 str!")
        if lucky_number%7==0:
            print("Du har tur och fick även +1 luck när du levlade upp!")
        if name.level%5==0:
            ("Du är extra stark nu och din hp har återgått till max!")
        Alternative()


def Escape_monster():
    tempo_luck = name.luck
    if name.luck >= 9:
        name.luck = 9
    Escape_chance = r.randint(0+(name.luck),10)
    name.luck = tempo_luck
    damage = r.randint(1+(3*name.level), 10+(3*name.level))

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
    try:
        if Spelare.luck == 1:
            chest_chance = r.randint(1, 10)
        elif Spelare.luck == 2: 
            chest_chance = r.randint(1+2*Spelare.luck, 10)
    except Exception as e:
        print("Error, name.luck in Room_chest had a problem") 
    
def Room_trap():
    print("Du öppnar dörren, och blir tagen i en fälla.\n ")
    damage = r.randint(10,40)/Spelare.luck
    Spelare.hp =- damage
    print(f"Du tog {damage} i skada")


# ALTERNATIV 
def Alternative():
    print(" (1) - Välj mellan 3 dörrar. \n (2) - Öppna inventory. \n (3) - Meny. \n (4) - Se Stats \n ")
    Answer = int(input("Ange vad du vill göra nu: "))
    if Answer == 1:
        Valt_rum()
    #elif Answer == 2:
        # Open_inv
    elif Answer == 3:
        Menu()
    elif Answer == 4:
        Stats()

def Stats():
    name.player_stats()
    Alternative()

# MENYN
def Menu():
    MenuLoop = 1
    while MenuLoop != 3:
        print(" ")
        print("(1) - Återuppta spelet")
        print("(2) - Avsluta spelet")
        
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
            print("Fel! Ange ett giltigt tal (1 eller 2)")             
def game_intro():
    #Skriver backstory
    intro_text = """"
Välkommen till spelet!
Du kommer få välja mellan att öppna dörrar som kommer kunna ha antingen monster, traps eller chests med loot som hjälper dig gå vidare
"""
    print_with_delay(intro_text)
    Alternative()
game_intro()