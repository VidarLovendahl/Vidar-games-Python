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
population = random.randint(10, 20)
food = random.randint(10, 100)
wood = random.randint(15, 60)
gold = random.randint(1, 30)
happiness = random.randint(40, 60)

# Misc variables
last_stranger_day = 0

# Settlement infrastructure
farms = 0
warehouses = 0
housing = 0
base_storage = 100
base_housing_capacity = 20

# Days
day = 1
max_days = 30 #int(input("How many days would you like to go for? "))
game_over = False

# Daily functions except end_day(), that will always be called last!
def cur_day():
    print("\n" + "=" * 30)
    print(f"       DAY {day}")
    print("=" * 30)

def show_status():
    print("=" * 30)
    print(f"Population: {population}")
    print(f"Food:       {food}")
    print(f"Wood:       {wood}")
    print(f"Gold:       {gold}")
    print(f"Happiness:  {happiness}")
    print(f"Max storage is: {base_storage + (warehouses * 50)}")
    print("=" * 30)

def action_menu():
    global food, wood, gold, happiness

    print("\nChoose your daily action:")
    print("1. Hunt for 25 food")
    print("2. Gather 10 wood")
    print("3. Trade 10 food for 15 gold")
    print("4. Hold a festival")
    print("5. Purchase settlement upgrades")

    choice = input(CYAN+"Enter your choice (1-5): "+RESET)

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
    elif choice == "5":
        upgrade_menu()

    else:
        print(RED+"Invalid choice! Try again."+RESET)
        action_menu()

def upgrade_menu():
    global wood, gold, farms, population, warehouses, housing

    print("\nChoose which upgrade you want to buy:")
    print("1. Farm - 40 wood, 20 gold")
    print("2. Warehouse - 50 wood, 15 gold")
    print("3. Housing - 30 wood, 10 gold")
    print("4. Back to main menu...")

    choice = input(CYAN+"Enter your choice (1-4): "+RESET)

    while choice not in ("1","2", "3", "4"):
        choice = input(CYAN+"Enter your choice (1-4): "+RESET)

    if choice == "1":
        if wood >= 40 and gold >= 20:
            wood -= 40
            gold -= 20
            farms += 1
            print("You built a farm!")
        else:
            print(RED+"You cannot afford this!"+RESET)

    elif choice == "2":
        if wood >= 50 and gold >= 15:
            wood -= 50
            gold -= 15
            warehouses += 1
            print("You built a warehouse!")
        else:
            print(RED+"You cannot afford this!"+RESET)

    elif choice == "3":
        if wood >= 30 and gold >= 10:
            wood -= 30
            gold -= 10
            housing += 1
            print("You built some housing!")
        else:
            print(RED+"You cannot afford this!"+RESET)

    elif choice == "4":
        print("Returning to main menu...")

# Event functions
def random_event():
    global food, wood, gold, happiness, population

    event_number = random.randint(1, 4)
    print(f"DEBUG: Event roll = {event_number}, Day = {day}")

    if event_number == 1:
        merchant_event()
        enforce_storage()
    elif event_number == 2:
        storm_event()
    elif event_number == 3:
        food += 25
        print(YELLOW+ "A good harvest gives the settlement 25 food!" +RESET)
        enforce_storage()
    elif event_number == 4:
        if day - last_stranger_day >= 5:
            stranger_event()
            enforce_storage()
        else:
            small_event()
            enforce_storage()

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
    choice = input(CYAN+ "Press 1 to reinforce buildings, costing 10 wood. Or press 2 and lose 5 wood and 10 gold. " +RESET)

    while choice not in ("1", "2"):
        print(RED+ "Invalid choice." +RESET)
        choice = input(CYAN+ "Press 1 to reinforce buildings, costing 10 wood. Or press 2 and lose 5 wood and 10 gold. " +RESET)

    if choice == "1":
        if wood >= 10:
            wood -= 10
            print("You reinforce your buildings with 10 wood.")
        else:
            print(RED+ "You cannot afford this." +RESET)
    elif choice == "2":
        wood -= 5
        gold -= 10
        print("The storm takes 5 wood and 10 gold.")

def stranger_event():
    global food, wood, population, gold, happiness, last_stranger_day, day

    last_stranger_day = day
    print(MAGENTA+ "A strange man comes to the settlement. Offering you his help." +RESET)
    choice = input(CYAN+ "Press 1 to accept the offer, or press 2 to decline it. " +RESET)

    while choice not in ("1", "2"):
        print(RED+ "Invalid choice." +RESET)
        choice = input(CYAN+ "Press 1 to accept the offer, or press 2 to decline it. " +RESET)

    if choice == "1":
        outcome = random.randint(1, 10)

        if outcome <= 5:
            food += 15
            gold += 10
            wood += 10
            happiness += 5
            print(YELLOW+ "The stranger smiles and gives the settlement his remaining resources!" +RESET)

        elif outcome <= 9:
            print("The stranger tells you not to  trust a lone man, and walks off into the sunset.")

        else:
            food -= 25
            gold -= 15
            wood -= 20
            happiness -= 10
            print(RED+ "The strange man's mouth widens in a grin, going on a rampage destroying tons of resources!" +RESET)


    elif choice == "2":
        print("You decline the offer and the stranger leaves with a sad look.")

def small_event():
    global food, wood, gold

    random_number = random.randint(1, 3)

    if random_number == 1:
        food += 10
        print(YELLOW+ "A settler managed to kill an ox for some extra food!"+RESET)

    elif random_number == 2:
        wood += 10
        print(YELLOW+"The settlers found a dead tree and chopped it up for some extra wood!"+RESET)

    elif random_number == 3:
        gold += 5
        print(YELLOW+"A little boy found a treasure chest by the beach, containing some gold!"+RESET)

# Misc funtions
def grow_population():
    global housing, base_housing_capacity, population

    max_housing_capacity = base_housing_capacity + (housing * 10)
    available_space = max_housing_capacity - population

    amount = random.randint(1, 4)
    new_settlers = min(amount, available_space)

    population += new_settlers

    if new_settlers == 0:
        print(YELLOW+ "No room for new settlers! Build more housing!" +RESET)

    elif new_settlers == 1:
        print(GREEN+ f"{new_settlers} settler arrived today! The settlement grows!" +RESET)
    else:
        print(GREEN+ f"{new_settlers} settlers arrived today! The settlement grows!" +RESET)

    if new_settlers < amount and new_settlers > 0:
        print(YELLOW+ f"{amount - new_settlers} potential settlers couldn't move in because there wasn't enough housing!" +RESET)

def enforce_storage():
    global food, wood, gold

    # Local variables
    max_storage = base_storage + (warehouses * 50)
    
    # Max storage check
    if food > max_storage:
        food = max_storage
    
    if wood > max_storage:
        wood = max_storage
    
    if gold > max_storage:
        gold = max_storage

def check_housing_capacity():
    global population, base_housing_capacity, housing
    max_housing_capacity = base_housing_capacity + (housing * 10)

    if population > max_housing_capacity:
        population = max_housing_capacity

def end_day():
    global food, wood, gold, happiness, population, game_over, farms, warehouses, housing

    # Farm bonus
    food += farms * 5

    # Enforce checks
    enforce_storage()
    check_housing_capacity()

    # Grow population
    if day % 2 == 0:
        grow_population()

    # Eating logic
    consumption = population//2
    print(f"The settlement consumes {consumption} food at the end of the day.")
    food -= consumption

    # Too little too late!
    if food <= 0:
        food = 0
        happiness -= 20
        population -= 1
        print(RED+ "There is not enough food! One settler has starved to death and the rest is unhappy!" +RESET)

    if population <= 0:
        population = 0
        print(RED+ "All settlers are dead! GAME OVER!!!" +RESET)
        game_over = True
#----------------------------------------#

while not game_over: # day <= max_days and
    cur_day()
    random_event()
    show_status()
    action_menu()
    end_day()

    if day == 30:
        print("The settlement survived for 30 days!")
        game_over = True

    day += 1

    input(CYAN+ "Press ENTER to start the next day..." +RESET)
