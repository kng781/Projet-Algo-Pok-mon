
from pokemonClass import Pokemon
import random 

Pokemon_characters = [
    Pokemon("Reshiram", 100, 200),
    Pokemon("Zekrom", 100, 200),
    Pokemon("Pikachu", 100, 27),
    Pokemon("Bulbizarre", 100, 78),
    Pokemon("Boustiflore", 100, 75),
    Pokemon("Salameche", 100, 92),
    Pokemon("Dracaufeu", 100, 59),
    Pokemon("Moustillon", 100, 69),
    Pokemon("Minidraco", 100, 93),
    Pokemon("Gruikui", 100, 91)
]

def choose_pokemon():
    print("Choisis ton Pokémon :")
    for i, p in enumerate(Pokemon_characters):
        print(f"{i+1}) {p.name} (PV: {p.hp}, Attaque: {p.attack_power})")

    while True:
        try:
            choice = int(input("Numéro du Pokémon : ")) - 1
            if 0 <= choice < len(Pokemon_characters):
                return choice
            else:
                print("Numéro incorrect, choisis un chiffre entre 1 et 10.")
        except ValueError:
            print("Entrée invalide ! Tape un nombre entre 1 et 10.")

def enemy_choosing(choice):
    enemies = Pokemon_characters[:choice] + Pokemon_characters[choice+1:]
    player_pokemon = Pokemon_characters[choice]
    enemy_pokemon = random.choice(enemies)
    print(f"Tu as choisi {player_pokemon.name} !")
    print(f"Ton adversaire a choisi {enemy_pokemon.name} !")
    return player_pokemon, enemy_pokemon




