import random

# Define the player's starting attributes
player = {
    "name": "",
    "class": "",
    "level": 1,
    "health": 100,
    "attack": 10,
    "defense": 5,
    "items": []
}

# Define the different classes and their attributes
classes = {
    "warrior": {
        "attack": 15,
        "defense": 10,
        "items": ["potion", "sword"]
    },
    "wizard": {
        "attack": 20,
        "defense": 5,
        "items": ["potion", "wand"]
    },
    # Add more classes here
}

# Define the enemies and their attributes
enemies = [
    {
        "name": "Goblin",
        "health": 30,
        "attack": 5,
        "defense": 2
    },
    {
        "name": "Skeleton",
        "health": 50,
        "attack": 8,
        "defense": 3
    },
    # Add more enemies here
]

# Define the function for generating a random enemy
def generate_enemy():
    return random.choice(enemies)

# Define the function for fighting an enemy
def fight(enemy):
    print("You encounter a", enemy["name"])
    while enemy["health"] > 0:
        action = input("Do you want to attack, defend, or use an item? ")
        if action == "attack":
            damage = player["attack"] - enemy["defense"]
            if damage > 0:
                print("You deal", damage, "damage to the", enemy["name"])
                enemy["health"] -= damage
            else:
                print("Your attack has no effect on the", enemy["name"])
        elif action == "defend":
            player["defense"] += 2
            print("You defend yourself against the", enemy["name"])
        elif action == "use item":
            # Implement code for using items here
            pass
        else:
            print("Invalid action. Please choose attack, defend, or use an item.")
        
        if enemy["health"] > 0:
            damage = enemy["attack"] - player["defense"]
            if damage > 0:
                print("The", enemy["name"], "deals", damage, "damage to you")
                player["health"] -= damage
            else:
                print("The", enemy["name"], "attacks you but does no damage")
        
        if player["health"] <= 0:
            print("Game over")
            break
    
    if player["health"] > 0:
        print("You defeated the", enemy["name"])
        player["level"] += 1
        print("You are now level", player["level"])

# Define the function for exploring
def explore():
    enemy = generate_enemy()
    fight(enemy)

# Start the game
print("Welcome to the text-based RPG game!")
player["name"] = input("What is your name? ")
player_class = input("Choose a class (warrior, wizard, etc): ")
if player_class in classes:
    player["class"] = player_class
    player["attack"] = classes[player_class]["attack"]
    player["defense"] = classes[player_class]["defense"]
    player["items"] = classes[player_class]["items"]
    print("You have chosen the", player_class, "class")
else:
    print("Invalid class. Please choose warrior, wizard, or another valid class")

while player["health"] >0:
    action = input("Do you want to explore, check your status, or quit? ")
    if action == "explore":
        explore()
    elif action == "check status":
        print("Name:", player["name"])
        print("Class:", player["class"])
        print("Level:", player["level"])
        print("Health:", player["health"])
        print("Attack:", player["attack"])
        print("Defense:", player["defense"])
        print("Items:", player["items"])
    elif action == "quit":
        print("Thanks for playing!")    
        break
    else:
        print("Invalid action. Please choose explore, check status, or quit.")
