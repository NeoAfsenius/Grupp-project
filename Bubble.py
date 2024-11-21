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

def game_intro():
    #Skriver backstory
    intro_text = """"
Välkommen till spelet!
Du kommer få välja mellan att öppna dörrar som kommer kunna ha antingen monster, traps eller chests med loot som hjälper dig gå vidare
"""
    print_with_delay(intro_text)
game_intro()

def Fight_monster():
    damage = r.randint(1+(3*name.level), 10+(3*name.level))
    if damage >= name.str:
        name.hp=name.hp-2*damage
        print("Du har nu" + str(name.hp) + "Hp")
    else:
        name.level=name.level+1
        name.str=name.str+2
        print("Du har vunnit och gått upp 1 level och 2 str!")

def Escape_monster():
    Escape_chance = r.randint(0,10)
    damage = r.randint(1+(3*name.level), 10+(3*name.level))

    print("Du försöker fly")
    if Escape_chance >= 3:
        print("Du lyckades att fly från monstret ")
    elif Escape_chance < 3:
        print(f"Du luckades inte att fly från monstret och därför )
        
        Menu()

        #Gå tillbaka till meny
def Valt_rum():
    int((input)"Välj mellan dörr 1,2,3")
    random_tal=r.randint(1,4)
    if random_tal = 1 :
        

    
def Room_monster():
    print("Du öppnar dörren, och ser ett monster.\n ")
    Monster_Action = input("Vill du fly eller attakera?")
    try:
        if Monster_Action.lower == "fly":
            Escape_monster()

        elif Monster_Action.lower == "attakera":
            Fight_monster()

    except Exception as e:
        print("Error, try again")
        Monster_Action = input("Vill du fly eller attakera?")

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


def Alternative():
    print("(1) - Välj mellan 3 dörrar. \n (2) - Öppna inventory. \n (3) - Meny. \n (4) - Se Stats")
    Answer = int(input("Ange vad du vill göra nu: "))
    if Answer == 1:
        Valt_rum()
    elif Answer == 2:
        # Open 
n
()vn
    elif Answer == 3:
        Menu()
    elif Answer == 4:
        Stats()

def Stats():
    player_stats()
    Alternative()

# MENYN
def Menu():
    MenuLoop = 1
    while MenuLoop != 3:
        print("(1) - Återuppta spelet")
        print("(2) - Avsluta spelet")
        
        try:
            MenuAnswer = int(input("Ange ditt val här: "))
            if MenuAnswer == 1:
                print("Återupptar spelet..")
                MenuLoop = MenuLoop + 2
                Alternative()
            elif MenuAnswer == 2:
                print("Avslutar spelet..")
                break 
            else:
                print("Ogiltigt val. Ange 1 eller 2")
        except ValueError:
            print("Fel! Ange ett giltigt tal (1 eller 2)")           

Alternative()