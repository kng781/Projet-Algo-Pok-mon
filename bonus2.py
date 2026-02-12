from pokemonClass import Pokemon
import random

# 1️⃣ Pokémon avec type
class PokemonType(Pokemon):
    def __init__(self, name, max_hp, attack_power, type):
        super().__init__(name, max_hp, attack_power)
        self.type = type

    def attack_target(self, target):
        damage = self.attack_power
        if self.type == "Feu" and target.type == "Plante":
            damage *= 2
        elif self.type == "Feu" and target.type == "Eau":
            damage //= 2
        elif self.type == "Eau" and target.type == "Feu":
            damage *= 2
        elif self.type == "Eau" and target.type == "Plante":
            damage //= 2
        elif self.type == "Plante" and target.type == "Eau":
            damage *= 2
        elif self.type == "Plante" and target.type == "Feu":
            damage //= 2

        target.take_damage(damage)
        print(f"{self.name} ({self.type}) attaque {target.name} ({target.type}) et inflige {damage} dégâts !")

# 2️⃣ Liste de Pokémon
Pokemon_characters_type = [
    PokemonType("Salameche", 100, 50, "Feu"),
    PokemonType("Bulbizarre", 100, 40, "Plante"),
    PokemonType("Carapuce", 100, 45, "Eau"),
    PokemonType("Pikachu", 100, 30, "Plante"),
    PokemonType("Gruikui", 100, 35, "Feu"),
    PokemonType("Moustillon", 100, 37, "Eau")
]

from pokemonClass import Pokemon

class TrainerType:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.active_pokemon = None

    def create_team(self):
        print(f"{self.name}, choisis ton équipe de 3 Pokémon :")
        team = []
        available = Pokemon_characters_type.copy()
        while len(team) < 3:
            for i, p in enumerate(available):
                print(f"{i+1}) {p.name} ({p.type}) (PV: {p.hp}, Attaque: {p.attack_power})")
            choice = int(input(f"Choix {len(team)+1}/3 : ")) - 1
            if 0 <= choice < len(available):
                team.append(available.pop(choice))
            else:
                print("Numéro incorrect.")
        self.team = team

    def choose_active_pokemon(self):
        print(f"{self.name}, choisis ton Pokémon actif :")
        for i, p in enumerate(self.team):
            print(f"{i+1}) {p.name} ({p.type}) (PV: {p.hp}/{p.max_hp})")
        choice = int(input("Numéro du Pokémon : ")) - 1
        self.active_pokemon = self.team[choice]
        print(f"{self.name} envoie {self.active_pokemon.name} !")

