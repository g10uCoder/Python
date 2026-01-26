"""
Simple Game using dictionaries, functions and conditions

"""
# Libraries
import random
import time
import math

# These two are optional, for beauty
from prettytable import PrettyTable
from colorama import Fore, Style, init

dungeon = dict()

# Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


# The information about player, weapons, enemies and sounds is accessed through these dictionaries
player = {
    "health": 100,
    "strength": 1,
    "weapon": "bare hands",
    "damage": 1,
    "room": 0
}

weapons = {
    "bare hands": 1,
    "pocket_knife": 2,
    "sword": 5,
    "mace": 10
}

weapon_sounds = {
    "bare hands": ["WHAM!", "THUD", "POW!", "CRACK!"],
    "pocket_knife": ["SHINKT!", "STAB!", "NICK!"],
    "sword": ["SHING", "SLASH!", "CLANG!"],
    "mace": ["CRUNCH!", "SMASH!", "THWACK!"]
}

# enemies with 0th index as health and 1st index as damage
enemies = {
    "skeleton": [10, 2],
    "zombie": [20, 4],
    "creaking": [40, 4],
    "ravager": [50, 5],
    "warden": [100, 10]
}

# game functionas
def create_dungeon():
    dungeon[1] = random.choice(["skeleton", "pocket_knife"])
    dungeon[2] = "pocket_knife" if dungeon[1] == "skeleton" else "skeleton"
    dungeon[3] = random.choice(["sword", "monster"])
    dungeon[4] = "sword" if dungeon[3] == "monster" else "monster"
    dungeon[5] = random.choice(["mace", "ravager"])
    dungeon[6] = "mace" if dungeon[5] == "ravager" else "ravager"
    dungeon[7] = "final boss"

def slow_print(string: str):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.025)


def choice_1():
    slow_print("Will you go to room 1 or 2? ")
    choice1 = input()
    if choice1 == "1":
        player["room"] = 1
        slow_print(RED + "You enter the first room.\n" + RESET)
    elif choice1 == "2":
        player["room"] = 2
        slow_print(RED + "You enter the second room.\n" + RESET)
    else:
        print("Grow UP!")
        choice_1()
    time.sleep(1.0)

def choice_2():
    slow_print("Will you choose room 3 or room 4? ")
    choice2 = input()
    if choice2 == "3":
        player["room"] = 3
        slow_print(RED + "You enter the third room.\n" + RESET)
    elif choice2 == "4":
        player["room"] = 4
        slow_print(RED + "You enter the fourth room.\n" + RESET)
    else:
        print("Grow UP!")
        choice_2()
    time.sleep(1.0)

def choice_3():
    slow_print("Will you go to room 5 or room 6? ")
    choice3 = input()
    if choice3 == "5":
        player["room"] = 5
        slow_print(RED + "You enter the fifth room.\n" + RESET)
    elif choice3 == "6":
        player["room"] = 6
        slow_print(RED + "You enter the sixth room.\n" + RESET)
    else:
        print("Grow UP!")
        choice_3()
    time.sleep(1.0)

def print_stats():
    print()
    time.sleep(1.0)
    if player["health"] > 0:
        print("----Current Player Stats----\n")
        time.sleep(2.0)
        table = PrettyTable()
        table.field_names = ["Stat", "Value"]
        # Adjusting keys for better readability in the table
        table.add_row(["Health", player["health"]])
        table.add_row(["Strength", player["strength"]])
        table.add_row(["Weapon", player["weapon"].replace("_", " ").title()])
        table.add_row(["Damage", player["damage"]])
        print(table)
    else:
        pass
    time.sleep(2.0)
    print()


def fight(enemy):
    info = enemies[enemy]
    hits = math.ceil(info[0] / player["damage"])
    print(RED + f"--- BATTLE: {enemy.upper()} ---" + RESET)
    time.sleep(0.5)
    for hit in range(hits):
        sfx = random.choice(weapon_sounds[player["weapon"]])
        print(YELLOW + sfx + RESET, end=" ", flush=True) 
        time.sleep(0.5)
    print()
    player["health"] -= hits * info[1]

def update_damage():
    player["damage"] = player["strength"] * weapons[player["weapon"]]

def interval():
    time.sleep(1.0)
    print()
    print(BLUE + "=================================================================================================" + RESET)
    time.sleep(1.0)

# Main game function
def game():
    create_dungeon()

    print("\n===========================================================================================================")

    choice_1()
    if dungeon[player["room"]] == "skeleton":
        print(RED + "What on earth? A skeleton?!" + RESET)
        time.sleep(1.0)
        fight("skeleton")
        time.sleep(0.5)
        print(GREEN + "Phew... that was easier than I expected." + RESET)
        time.sleep(1.0)
        slow_print(GREEN + "The skeleton collapses into a heap of dust and bone.\n" + RESET)
        print_stats()
        time.sleep(1.0)
        interval()
    else:
        player["weapon"] = "pocket_knife"
        player["strength"] += 1
        slow_print(YELLOW + "You discovered a Monster Energy drink!\n" + RESET + GREEN + "(+1 Strength)")
        slow_print(BLUE + "You found a pocket knife. It deals double your strength in damage.\n" + RESET)
        update_damage()
        time.sleep(1.0)
        print(GREEN + "Finally, something I can actually use!" + RESET)
        time.sleep(1.0)
        slow_print(RED + "You proceed.\n" + RESET)
        print_stats()
        interval()


    choice_2()
    if dungeon[player["room"]] == "sword":
        player["weapon"] = "sword"
        slow_print(BLUE + "You retrieved a sturdy sword. Your strength is now amplified fivefold.\n" + RESET)
        time.sleep(0.5)
        if player["weapon"] == "pocket_knife":
            print(BLUE + "This is a massive upgrade!" + RESET)
        else:
            print(BLUE + "At last! A real weapon!" + RESET)
        update_damage()
        time.sleep(0.5)
        slow_print(RED + "A rotting zombie lunges from the shadows!\n" + RESET)
        time.sleep(0.5)
        fight("zombie")
        slow_print(GREEN + "You slaughtered the zombie and wiped the blood from your blade.\n" + RESET)
        print_stats()
        time.sleep(1.0)
        print()

        slow_print(RED + "Before you proceed, would you like to enter the secret room? (1: Yes, anything else: No) " + RESET)
        s = input()
        time.sleep(0.5)

        if s == "1":
            print(YELLOW + "Sweet! A Monster drink. Just what I needed." + RESET)
            time.sleep(1.0)
            slow_print(YELLOW + "You down the drink. You feel your muscles grow stronger.\n" + RESET)
            time.sleep(0.5)
            slow_print(RED + "A withered creaking blocks your path. You cannot ignore it!\n" + RESET)
            fight("creaking")
            slow_print(GREEN + "You leave the room destroying its heart and continue your journey.\n" + RESET)
            time.sleep(1.0)
            print_stats()
            interval()
            choice_3()
        else:
            slow_print("And you move further into the dungeon...")
            time.sleep(1.0)
            choice_3()
    else:
        print(YELLOW + "Yes! A Monster drink!" + RESET + GREEN + "(+1 Strength)")
        player["strength"] += 1
        update_damage()
        time.sleep(0.5)
        print_stats()
        time.sleep(0.5)
        slow_print(RED + "You press on, deeper into the dungeon.\n" + RESET)
        time.sleep(1.0)
        interval()
        choice_3()

    if dungeon[player["room"]] == "mace":
        slow_print(BLUE + "You discover the legendary Mace. Your strength is now amplified tenfold.\n" + RESET)
        player["weapon"] = "mace"
        update_damage()
        print(BLUE + "Whoa... this thing is heavy, but it packs a punch." + RESET)
        time.sleep(1.0)
        print_stats()
        time.sleep(1.0)
        slow_print(RED + "The air grows cold. Are you ready for the Boss?\n" + RESET)
        interval()
        time.sleep(1.0)
        slow_print(RED + "Out of the darkness, the WARDEN emerges!\n" + RESET)
        time.sleep(1.0)
        player["room"] = 7
        fight("warden")
        time.sleep(5.0)
        if player["health"] <= 0:
            print(RED + "No... this can't be how it ends..." + RESET)
            time.sleep(1.0)
            slow_print(RED + "You were no match for the Warden's power.\n" + RESET)
            interval()
            slow_print("Would you like to try again? (1: Yes, anything else: No) " + RESET)
            again = input()
            if again == "1":
                interval()
                game()
            else:
                pass
        else:
            print(GREEN + "Haha! I actually did it! I'm alive!" + RESET)
            time.sleep(1.0)
            slow_print(GREEN + "The Warden falls with a deafening thud.\n YOU ARE VICTORIOUS!!!\n" + RESET)
            interval()
            slow_print(GREEN + "Would you like to play again? (1: Yes, anything else: No) " + RESET)
            again = input()
            if again == "1":
                interval()
                game()
            else:
                pass

    else:
        slow_print(YELLOW + "You find a Monster drink. You drink it and feel a surge of adrenaline.\n" + RESET)
        print(YELLOW + "I feel unstoppable now!" + RESET)
        player["strength"] += 1
        update_damage()
        time.sleep(1.0)
        print_stats()
        time.sleep(1.0)
        print(RED + "Wait... what's that sound?" + RESET)
        time.sleep(1.0)
        slow_print(RED + "A ferocious Ravager charges toward you!\n" + RESET)
        fight("ravager")
        if player["health"] <= 0:
            print(RED + "Nooooo! Not like this!" + RESET)
            time.sleep(1.0)
            slow_print(RED + "That wasn't even the boss! Were you too exhausted to fight?\n" + RESET)
            interval()
            slow_print("Would you like to try again? (1: Yes, anything else: No) " + RESET)
            again = input()
            if again == "1":
                interval()
                game()
            else:
                pass
        else:
            time.sleep(1.0)
            slow_print(GREEN + "You survived, but the worst is yet to come. Ready for the Boss?\n" + RESET)
            print_stats()
            time.sleep(1.0)
            slow_print(RED + "The WARDEN has arrived!\n" + RESET)
            time.sleep(1.0)
            player["room"] = 7
            fight("warden")
            time.sleep(5.0)
            if player["health"] <= 0:
                print(RED + "Everything is going dark..." + RESET)
                time.sleep(1.0)
                slow_print(RED + "The Warden was too powerful for you to overcome.\n" + RESET)
                interval()
                slow_print("Would you like to try again? (1: Yes, anything else: No) " + RESET)
                again = input()
                if again == "1":
                    interval()
                    game()
                else:
                    pass
            else:
                print(GREEN + "I'm the king of this dungeon!" + RESET)
                time.sleep(1.0)
                slow_print(GREEN + "You have defeated the Warden and earned your freedom!\n" + RESET)
                interval()
                slow_print(GREEN + "Would you like to play again? (1: Yes, anything else: No) " + RESET)
                again = input()
                if again == "1":
                    interval()
                    game()
                else:
                    pass

start = """
You are trapped in a dark, damp dungeon. At every turn, you must make a choice. 
Select one path and abandon the other. To escape, you must scavenge for supplies, 
slay monsters, and pray for good fortune!

Caffeine is your friend: gain 1 Strength point for every Monster Energy drink you find.
Weapons will amplify your base strength to deal devastating damage.

"""



slow_print(start)
print("You Start with these stats:")
print_stats()
slow_print("Enjoy!")
game()

    




    

