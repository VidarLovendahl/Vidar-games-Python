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

# Starting resources
population = random.randint(20, 50)
food = random.randint(50, 150)
gold = random.randint(20, 80)
happiness = random.randint(40, 90)
wood = random.randint(30, 120)
score = 0

# Starting message
print("=" * 35)
print("       THE CHAOS SIMULATOR")
print("=" * 35)

# Starting resources
print(f"Population: {population}")
print(f"Food: {food}")
print(f"Wood: {wood}")
print(f"Gold: {gold}")
print(f"Happiness: {happiness}")

# Days
day = 0
maxDays = int(input("How many days would you like to simulate? "))

# Events: message, resource, amount, chance currently 100%

events = [
    ("Its a calm day, nothing happens.", {}, 20),

    (YELLOW + "A merchant donates 20 gold!" + RESET,
     {"gold": 20}, 5),

    (RED + "A thief steals 15 gold!" + RESET,
     {"gold": -15}, 5),

    (YELLOW + "A good harvest provides 25 food!" + RESET,
     {"food": 25}, 15),

    (RED + "A plague destroys the harvest!" + RESET,
     {"food": -20}, 10),

    (YELLOW + "A festival raises happiness!" + RESET,
     {"happiness": 15}, 5),

    (RED + "A boring week lowers happiness!" + RESET,
     {"happiness": -10}, 5),

    (YELLOW + "New settlers arrive!" + RESET,
     {"population": 5}, 5),

    (RED + "Some settlers leave the village." + RESET,
     {"population": -3}, 5),

    (MAGENTA + "A meteor strikes the settlements food supply!" + RESET,
     {"food": -35}, 2),

    (YELLOW + "A settler has found a gold vein!" + RESET,
     {"gold": 50}, 3),

    (RED + "A virus spreads amongst the livestock!" + RESET,
     {"food": -10}, 5),

    (YELLOW + "The settlers have found a mushroom spot!" + RESET,
     {"food": 15}, 5),

    (MAGENTA + "The settlers are trying cannibalism..." + RESET,
     {"food": 10, "happiness": -10, "population": -5}, 2),

    (YELLOW + "The settlers chopped some wood." + RESET,
     {"wood": 20}, 4),

    (RED + "A small fire started in the wood supply!" + RESET,
     {"wood": -15}, 4)
]


# Random events each day
for day in range(1, maxDays + 1):
    input("\nPress ENTER to begin the next day...")
    print(f"\n--- DAY {day} ---")

    
    # Select a random event using its probability weight
    event = random.choices(
        events,
        weights=[e[2] for e in events],
        k=1
    )[0]

    # Display the event message
    print(event[0])

    # Apply every resource change from the event
    for resource, amount in event[1].items():
        if resource == "food":
            food += amount
        elif resource == "gold":
            gold += amount
        elif resource == "happiness":
            happiness += amount
        elif resource == "population":
            population += amount
        elif resource == "wood":
            wood += amount

    # Daily food consumption
    food -= population // 2

    # Hunger makes people unhappy
    if food < 0:
        print(RED + "The settlement is starving!" + RESET)
        happiness -= 10
        food = 0

    # Unhappy people may leave
    if happiness < 20 and population > 0:
        population -= min(2, population)
        print(RED + "Some unhappy settlers leave!" + RESET)

    # When reaching 100 gold, rewards are given
    if gold >= 100:
        population += 5
        food += 20
        happiness += 15
        gold = 15
        print(GREEN + "The settlment buys some resources with their gold!" + RESET)

    # A lot of food makes people happy
    if food >= 75:
        happiness += 5
        print(GREEN + "Everyone gets to eat!" + RESET)

    # A lot of gold makes people happy
    if gold >= 65:
        happiness += 10
        print(GREEN + "There are no taxes today!" + RESET)

    # Keep values within sensible limits
    population = max(0, population)
    gold = max(0, gold)
    food = max(0, food)
    happiness = max(0, min(100, happiness))

    print(
        f"Population: {population} | "
        f"Food: {food} | Gold: {gold} | "
        f"Happiness: {happiness}"
    )

    # Score is counted on the final amount of resources and the current day
    score = population + food + gold + happiness + day

    if population == 0:
        print(RED + f"\nTHE SETTLEMENT HAS COLLAPSED! With a score of {score}" + RESET)
        break

else:
    print(YELLOW + f"\nThe settlement survived all 30 days! With a score of {score}!" + RESET)