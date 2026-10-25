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
population = 20
food = 100
wood = 30
gold = 50
happiness = 70

# Days
day = 1
max_days = 30 #int(input("How many days would you like to go for? "))


def show_status():
    print("\n" + "=" * 30)
    print(f"       DAY {day}")
    print("=" * 30)
    print(f"Population: {population}")
    print(f"Food:       {food}")
    print(f"Wood:       {wood}")
    print(f"Gold:       {gold}")
    print(f"Happiness:  {happiness}")
    print("=" * 30)


def action_menu():
    global food, wood, gold, happiness

    print("\nChoose your daily action:")
    print("1. Hunt for 15 food")
    print("2. Gather 10 wood")
    print("3. Trade 10 food for 15 gold")
    print("4. Hold a festival")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        food += 15
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
        gold += 10
        print(YELLOW+ "A traveling merchant arrives and gives the settlement 10 gold!" +RESET)
    elif event_number == 2:
        wood -= 5
        print(YELLOW+ "A storm damages the settlement, causing them to lose 5 wood!" +RESET)
    elif event_number == 3:
        food += 20
        print(YELLOW+ "A good harvest gives the settlement 20 food!" +RESET)


#----------------------------------------#

while day <= max_days:
    random_event()
    show_status()
    action_menu()

    day += 1