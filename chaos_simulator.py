import random

# Starting resources
population = random.randint(20, 50)
food = random.randint(50, 150)
gold = random.randint(20, 80)
happiness = random.randint(40, 90)
score = 0

# Starting message
print("=" * 35)
print("       THE CHAOS SIMULATOR")
print("=" * 35)

# Starting resources
print(f"Population: {population}")
print(f"Food: {food}")
print(f"Gold: {gold}")
print(f"Happiness: {happiness}")

# Days
day = 0
maxDays = int(input("How many days would you like to simulate? "))

# Events
events = [
    ("Its a calm day, nothing happens.", "gold", 0),
    ("Its a calm day, nothing happens.", "gold", 0),
    ("Its a calm day, nothing happens.", "gold", 0),
    ("A merchant donates 20 gold!", "gold", 20),
    ("A thief steals 15 gold!", "gold", -15),
    ("A good harvest provides 25 food!", "food", 25),
    ("A plague destroys the harvest!", "food", -20),
    ("A festival raises happiness!", "happiness", 15),
    ("A boring week lowers happiness!", "happiness", -10),
    ("New settlers arrive!", "population", 5),
    ("Some settlers leave the village.", "population", -3),
    ("A meteor strikes the settlements food supply!", "food", -35),
    ("A settler has found a gold vein!", "gold", 50),
    ("A virus spreads amongst the livestock!", "food", -10),
    ("The settlers have found a mushroom spot!", "food", 15),
    ("The settlers are trying cannibalism...", "food", 10, "happiness", -10, "population", -5),
    # Add a way to change the probability on getting different events
    ]

# Random events each day
for day in range(1, maxDays + 1):
    print(f"\n--- DAY {day} ---")

    event = random.choice(events)
    print(event[0])

    if event[1] == "gold":
        gold += event[2]
    elif event[1] == "food":
        food += event[2]
    elif event[1] == "happiness":
        happiness += event[2]
    elif event[1] == "population":
        population += event[2]


    # Daily food consumption
    food -= population // 3

    # Hunger makes people unhappy
    if food < 0:
        print("The settlement is starving!")
        happiness -= 10
        food = 0

    # Unhappy people may leave
    if happiness < 20 and population > 0:
        population -= min(2, population)
        print("Some unhappy settlers leave!")

    # When reaching 100 gold, rewards are given
    if gold >= 100:
        population += 5
        food += 20
        happiness += 15
        gold = 15
        print("The settlment buys some resources with their gold!")

    # A lot of food makes people happy
    if food >= 75:
        happiness += 5
        print("Everyone gets to eat!")

    # A lot of gold makes people happy
    if gold >= 65:
        happiness += 10
        print("There are no taxes today!")

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
        print(f"\nTHE SETTLEMENT HAS COLLAPSED! With a score of {score}")
        break

else:
    print(f"\nThe settlement survived all 30 days! With a score of {score}!")
