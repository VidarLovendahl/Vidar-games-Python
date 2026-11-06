# Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
# Example:  print(RED + "Error!" + RESET)

import random

# PLAYER STATS
player_health = random.randint(75, 100)
player_damage = random.randint(10, 20)
max_health = player_health

# ENEMY STATS
enemy_health = 0
enemy_damage = 0
enemy_damage_multiplier = 1

# VARIABLES
battle_count = 1

# FUNCTIONS
def player_choices():
    global player_health, enemy_health, player_damage, enemy_damage, battle_count, enemy_damage_multiplier

    while player_health > 0 and enemy_health > 0:
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Heal")
        print("3. Run")
        choice = input(CYAN + "\nEnter your choice (1, 2, or 3): " + RESET)
        if choice not in ["1", "2", "3"]:
            print(RED + "\nInvalid choice! Please try again." + RESET)
            return player_choices()

        if choice == "1":
            print(GREEN + "\nYou chose to attack!" + RESET)
            enemy_health -= player_damage
            print(RED + f"\nYou dealt {player_damage} damage to the enemy!" + RESET)
            print(RED + f"\nEnemy health is now {enemy_health}." + RESET)

        elif choice == "2":
            print(GREEN + "\nYou chose to heal!" + RESET)
            player_health += 20
            if player_health > max_health:
                player_health = max_health
            print(GREEN + f"\nYou healed for 20 health!" + RESET)

        elif choice == "3":
            print(GREEN + "\nYou chose to run!" + RESET)
            print(RED + "\nYou ran away from the battle!" + RESET)
            newbattle()

        print(RED + f"\nThe enemy dealt {enemy_damage} damage to you!" + RESET)
        player_health -= enemy_damage
        print(GREEN + f"\nYour health is now {player_health}." + RESET)

        if enemy_health <= 0:
            print(GREEN + "\nYou defeated the enemy!" + RESET)
            battle_count += 1
            battle_upgrade()
            newbattle()

        if player_health <= 0:
            print(RED + "\nYou have been defeated!" + RESET)
            print(RED + "\nGame Over!" + RESET)
            exit()

def newbattle():
    global enemy_health, enemy_damage, battle_count

    enemy_health = random.randint(20, 100)
    enemy_damage = random.randint(5, 15) * enemy_damage_multiplier
    print("=" * 30)
    print(YELLOW + f"\nBattle: {battle_count}" + RESET)
    print("=" * 30)
    print(YELLOW + f"\nA new enemy has appeared with {enemy_health} health and {enemy_damage} damage!" + RESET)
    player_choices()

def show_status():
    print(YELLOW + f"\nYour health: {player_health}" + RESET)
    print(YELLOW + f"\nYour damage: {player_damage}" + RESET)

def upgrade_player():
    global player_health, player_damage

    print(CYAN + "\nWhat would you like to upgrade?" + RESET)
    print("1. Increase your damage by 5")
    print("2. Increase your health by 10")
    upgrade_choice = input(CYAN + "\nEnter your choice (1 or 2): " + RESET)

    if upgrade_choice == "1":
        player_damage += 5
        print(GREEN + f"\nYour damage has been increased to {player_damage}!" + RESET)
    elif upgrade_choice == "2":
        max_health += 10
        player_health = max_health
        print(GREEN + f"\nYour health has been increased to {player_health}!" + RESET)
    else:
        print(RED + "\nInvalid choice! Please try again." + RESET)
        upgrade_player()

def battle_upgrade():
    global enemy_damage_multiplier

    if battle_count % 5 == 0:
        print(GREEN + "\nYou have now defeated 5 enemies, you can now choose an upgrade!" + RESET)
        print(RED + "\nThe enemy damage multiplier has increased!" + RESET)

        enemy_damage_multiplier += 0.5
        upgrade_player()

# GAME LOOP
print("Welcome to the Battle Simulator!")
print("=" * 50)
print("Here you will face off against a randomly generated enemy.")
input(CYAN + "Press Enter to start the game!" + RESET)

show_status()
input(CYAN + "\nPress Enter to face your enemy!" + RESET)

newbattle()