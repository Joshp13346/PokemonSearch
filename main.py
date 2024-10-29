'''
Josh Phillips
4/20/24
CS424-01
This program requires the user to enter a CSV filled with Pokemon Cards, loading them into an array of objects.
Then, the user is prompted to input search criteria (requests specific format separated by 6 commas (",,,,,," would be an empty search))
Search Criteria: Type, Minimum Attack Damage, HP, Ablities, Stage, Attack Energy Amount, Attack Energy Type
The program then outputs the results to the user, and prompts the user to either 'exit' or continue searching for Pokemon
Steps (Each step is prompted in the command line, this is just a recap):
    1   Start program
    2   Enter CSV file path or just the file name if in the same directory
    3   To continue with searching, hit enter. To exit, type 'exit'
    4   Enter comma separated list of 7 search parameters (again, ",,,,,," indicates no search parameters, "Grass,,,,,," would return all Grass type)
    5   Repeat steps 3 and 4
'''

import csv

class Pokemon:
    def __init__(self, name, hp, type, stage, evolvesFrom, attacks, ability, retreatCost):
        self.name = name
        self.hp = hp
        self.type = type
        self.stage = stage
        self.evolvesFrom = evolvesFrom
        self.attacks = attacks
        self.ability = ability
        self.retreatCost = retreatCost
    def __repr__(self):
        return f"Name: {self.name} \nHP: {self.hp} \nType: {self.type} \nStage: {self.stage} \nEvolves From: {self.evolvesFrom} \nAttacks: {self.attacks} \nAbility: {self.ability} \nRetreat Cost: {self.retreatCost}"

class Attack:
    def __init__(self, name, description, damage, energy):
        self.name = name
        self.description = description
        self.damage = damage
        self.energy = energy
    def __repr__(self):
        return f"Name: {self.name} \nDescription: {self.description} \nDamage: {self.damage} \nEnergy: {self.energy}"

class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"Name: {self.name} \nDescription: {self.description}"      

# Reads in CSV, loading the pokemon cards into the array as objects
# Also handles the potential multiple attacks and abilities
def read_csv(file_path):
    pokemon_cards = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                attacks = []
                ability = None
                if row:
                    if "{" in row[5]:   # Check if there are attacks
                        attack_info = eval(row[5])
                        for attack in attack_info:
                            attack = {key.lower(): value for key, value in attack.items()}
                            if attack["damage"]:
                                attack["damage"] = int(''.join(filter(lambda x: x.isdigit(), attack["damage"])))    # Filter num out of string
                            else:
                                attack["damage"] = 0    # Avoids failures for '' and int comparisons
                            attacks.append(Attack(**attack))

                    if "{" in row[6]:   # Check if there are abilities
                        ability_info = eval(row[6])
                        ability_info = {key.lower(): value for key, value in ability_info.items()}
                        ability = Ability(**ability_info)
                    
                    pokemon_cards.append(Pokemon(row[0], row[1], row[2], row[3], row[4], attacks, ability, row[7]))
        file_exists = True

    except FileNotFoundError:
        print(f"File not found at path: {file_path}.")
        file_exists = False

    return pokemon_cards,file_exists

# Takes in original pokemon cards and user input search criteria, filters by criteria and returns temp_cards with filtered cards
def search(pokemon_cards, search_criteria): 
    temp_cards = []
    params = search_criteria.split(",") # Loads user input criteria into params
    if params[1]:
        params[1] = int(params[1])
    
    for pokemon in pokemon_cards:   # Checks each pokemon, if all criteria pass, append to temp_cards
        if pokemon and pokemon.name != "Name":
            pokemon: Pokemon = pokemon
            failed = False
            # Search Type
            if params[0] and not (pokemon.type.lower() == params[0].lower()):
                failed = True
            # Search Minimum Attack Damage    
            for attack in pokemon.attacks:
                if params[1] and not (attack.damage >= params[1]):
                    failed = True
            # Search HP
            if params[2] and not (pokemon.hp == params[2]):
                failed = True
            # Search Abilities
            if params[3] and not (pokemon.ability and params[3].lower() == pokemon.ability.name.lower()):
                failed = True
            # Search Stage
            if params[4] and not (pokemon.stage.lower() == params[4].lower()):
                failed = True
            for attack in pokemon.attacks:
                attack: Attack = attack
                # Search Attack Energy Amount
                for energy in attack.energy:
                    if params[5] and not (attack.energy[energy] == int(params[5])):
                        failed = True
                    # Search Attack Energy Type
                    if params[6] and not (energy.lower() == params[6].lower()):
                        failed = True
            if not failed:
                temp_cards.append(pokemon)
    return temp_cards

file_exists = False
#   Terminates once user has entered a valid file / file path
while file_exists == False:
    file_path = input("Enter file path to csv: ")   # User inputs file path to CSV
    pokemon_cards,file_exists = read_csv(file_path)

#   Allows user to search as many times as they want before exiting the program
while input("To search, press enter, to exit, type 'exit': ") != "exit":
    search_criteria = input("Search by Type, Minimum Attack Damage, HP, Ablities, Stage, Attack Energy Amount, Attack Energy Type\n" +
                        "Please format your responce with all categories, including empty (ie Fire,,,,,,): ")
    searched_pokemon_cards = []
    searched_pokemon_cards = search(pokemon_cards, search_criteria)
    print("Results:")
    for card in searched_pokemon_cards:
        print(card)
        print('\n')
