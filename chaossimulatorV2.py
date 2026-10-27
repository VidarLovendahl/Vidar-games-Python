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

# Settlement resources
population = random.randint(10, 50)
food = random.randint(10, 100)
wood = random.randint(15, 60)
gold = random.randint(1, 30)
happiness = random.randint(40, 60)

# Days
day = 1
max_days = 30 #int(input("How many days would you like to go for? "))
game_over = False

def cur_day():
    print("\n" + "=" * 30)
    print(f"       DAY {day}")
    print("=" * 30)

def show_status():
    print(f"Population: {population}")
    print(f"Food:       {food}")
    print(f"Wood:       {wood}")
    print(f"Gold:       {gold}")
    print(f"Happiness:  {happiness}")
    print("=" * 30)


def action_menu():
    global food, wood, gold, happiness

    print("\nChoose your daily action:")
    print("1. Hunt for 25 food")
    print("2. Gather 10 wood")
    print("3. Trade 10 food for 15 gold")
    print("4. Hold a festival")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        food += 25
        print("You went hunting!")

    elif choice == "2":
        wood += 10
        print("You gathered wood!")

    elif choice == "3":
        if food < 10:
            print("You cannot perform this action!")
        else:
            food -= 10
            gold += 15
            print("You traded with a merchant!")

    elif choice == "4":
        if gold < 10:
            print("You cannot perform this action!")
        else:
            gold -= 10
            happiness += 15
            print("You held a festival!")

    else:
        print("Invalid choice! Try again.")


def random_event():
    global food, wood, gold, happiness, population

    event_number = random.randint(1, 3)

    if event_number == 1:
        merchant_event()
    elif event_number == 2:
        storm_event()
    elif event_number == 3:
        food += 25
        print(YELLOW+ "A good harvest gives the settlement 20 food!" +RESET)


def end_day():
    global food, happiness, population, game_over

    print(f"The settlement consumes {population} food at the end of the day.")
    food -= population//2

    if food <= 0:
        food = 0
        happiness -= 20
        population -= 1
        print(RED+ "There is not enough food! One settler has starved to death and the rest is unhappy!" +RESET)

    if population <= 0:
        population = 0
        print(RED+ "All settlers are dead! GAME OVER!!!" +RESET)
        game_over = True

def merchant_event():
    global food, gold

    print(YELLOW+ "A travelling merchant has arrived!" +RESET)
    print(YELLOW+ "They offer 40 food for 20 gold." +RESET)

    choice = input(CYAN+ "Press 1 to accept, or press 2 to decline. " +RESET)

    while choice not in ("1", "2"):
        print(RED+ "Invalid choice." +RESET)
        choice = input(CYAN+ "Press 1 to accept, or press 2 to decline. " +RESET)

    if choice == "1":
        if gold >= 20:
            food += 40
            gold -= 20
            print("A good deal!")
        else:
            print(RED+ "You cannot afford this deal." +RESET)

    elif choice == "2":
        print("You decline the offer.")

def storm_event():
    global wood, gold

    print(YELLOW+ "A storm is coming!" +RESET)
    choice = input(CYAN+ "Press 1 to reinforce buildings, cost 10 wood. Or press 2 and lose 5 wood and 10 gold. " +RESET)

    while choice not in ("1", "2"):
        print(RED+ "Invalid choice." +RESET)
        choice = input(CYAN+ "Press 1 to reinforce buildings, cost 10 wood. Or press 2 and lose 5 wood and 10 gold. " +RESET)

    if choice == "1":
        if wood >= 10:
            wood -= 10
            print("You reinforce your buildings for 10 wood.")
        else:
            print(RED+ "You cannot afford this." +RESET)
    elif choice == "2":
        wood -= 5
        gold -= 10
        print("The storm takes 5 wood and 10 gold.")


#----------------------------------------#

while not game_over: # day <= max_days and 
    cur_day()
    random_event()
    show_status()
    action_menu()
    end_day()

    if day == 30:
        print("The settlement survived for 30 days!")

    day += 1

    input(CYAN+ "Press ENTER to start the next day..." +RESET)
