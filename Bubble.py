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
    def __init__(self, strength_bonus, health_bonus, luck_bonus, namn):
        self.str_bonus = strength_bonus
        self.hp_bonus = health_bonus
        self.luck_bonus = luck_bonus
        self.name = namn

def create_sword():
    return Item(2,2,0,"sword")

def create_belt():
    return Item(0,5,0, "belt")

def create_potion():
    return Item(15,0,0, "potion")

def create_luckybraclet():
    return Item(0,0,2, "braclet")

def create_unluckyboots():
    return Item(0,-10,0, "boots")


player = input("Spelarens namn: ") 
player = Spelare(100, 10, 1, 1, player)
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
    monster_damage = r.randint(1+(2*player.level), 10+(2*player.level))
    if monster_damage >= player.str:
        player.hp = player.hp-2*monster_damage
        print("Du förlorade och tog skada")
        print(f"Du har nu {player.hp} Hp")
        print("")
        Alternative()
    elif monster_damage == player.str:
        print("Ni är lika starka, du går vidare")
        Alternative()
    if monster_damage <= player.str:
        player.level = player.level + 1
        player.str= player.str + 2
        lucky_number = r.randint(1,7)
        print("Du vann över monstret och gick upp i Level och din str gick upp 2 enheter")
        if lucky_number%7==0:

            player.luck=+ 1
            print("Du har tur och fick även +1 luck när du levlade upp!")
        Alternative()

def Escape_monster():
    tempo_luck = player.luck
    if player.luck >= 9:
        player.luck = 9
    Escape_chance = r.randint(0+(player.luck),10)
    player.luck = tempo_luck
    escape_damage = r.randint(1+(3*player.level), 10+(3*player.level))

    print("Du försöker fly")
    if Escape_chance >= 5:
        print("Du lyckades att fly från monstret ")
        Alternative()
    elif Escape_chance < 5:
        print("Du lyckades inte att fly från monstret och därför tog du skada")
        escape_damage = r.randint(10 , 20-(player.luck))
        player.hp=player.hp - escape_damage
        print("Du tog " + str(escape_damage) + " Skada")
        print("Du har nu " + str(player.hp) +  "HP")
        Alternative()

def Room_chest():
    print("Du öppnar dörren, och ser en kista.\n ")

    #Nödvädnigt med try?
    if player.luck == 1:
        chest_chance = r.randint(1, 20)
    elif player.luck == 2: 
        chest_chance = r.randint(1+2*player.luck, 20)
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
    player.hp =- damage
    print(f"Du tog {damage} i skada")
    Alternative()

# ALTERNATIV 
def Alternative():
    if player.hp > 0:
        print(" [1] - Välj mellan 3 dörrar. \n [2] - Öppna inventory. \n [3] - Meny. \n [4] - Se Stats \n ")
        try:
            Answer = int(input("Ange vad du vill göra nu: "))
            if Answer == 1:
                Valt_rum()
            elif Answer == 2:
                player.show_inventory()
            elif Answer == 3:
                Menu()
            elif Answer == 4:
                player.player_stats()
            elif Answer < 1 or Answer > 4:
                print("\n Fel! Ange ett giltigt tal 1-4")
                Alternative()
        except ValueError:
            print("\n Fel! Ange ett giltigt tal 1-4")
            Alternative()
    if player.hp < 0: 
        print("Du förlorade!")

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
    try:
        g = int(input("""
Välj dörr
Dörr 1:
Dörr 2:
Dörr 3:
"""))
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
        print("\nFel! Ange ett giltigt heltal mellan 1-3")
        Valt_rum()  


def game_intro():
    #Skriver backstory
    intro_text = f"""
Välkommen till spelet, {player.name}!
Du kommer få välja mellan att öppna dörrar som kan innehålla monster, fällor,
eller kistor med loot som hjälper dig att gå vidare.
"""

    print_with_delay(intro_text)
    Alternative()

game_intro()