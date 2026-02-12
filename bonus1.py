from characters import Pokemon, Pokemon_characters
import random

class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.active_pokemon = None
        

    def create_team(self):
        print(f"{self.name}, choisis ton équipe de 3 Pokémons :\n")
        team = []
        available = Pokemon_characters.copy()  # copie de la liste complète
        while len(team) < 3:
            print("Liste des Pokémon disponibles :")
            for i, p in enumerate(available):
                print(f"{i+1}) {p.name} (PV: {p.hp}, Attaque: {p.attack_power})")
            try:
                choice = int(input(f"Choix {len(team)+1}/3 : ")) - 1
                if 0 <= choice < len(available):
                    team.append(available.pop(choice))  # retire le Pokémon choisi
                    print(f"{team[-1].name} ajouté à ton équipe.\n")
                else:
                    print("Numéro incorrect.\n")
            except ValueError:
                print("Entrée invalide ! Tape un nombre.\n")
        self.team = team
        return team

    def choose_active_pokemon(self):
        while True:
            print(f"{self.name}, choisis ton Pokémon actif :")
            for i, p in enumerate(self.team):
                status = "K.O." if p.is_defeated() else f"{p.hp}/{p.max_hp} PV"
                print(f"{i+1}) {p.name} ({status})")
            try:
                choice = int(input("Numéro du Pokémon : ")) - 1
                if 0 <= choice < len(self.team):
                    if not self.team[choice].is_defeated():
                        self.active_pokemon = self.team[choice]
                        print(f"{self.name} envoie {self.active_pokemon.name} !\n")
                        return
                    else:
                        print(f"{self.team[choice].name} est K.O., choisis un autre Pokémon !")
                else:
                    print(f"Numéro incorrect, choisis entre 1 et {len(self.team)}.")
            except ValueError:
                print("Entrée invalide ! Tape un nombre.")

    def all_defeated(self):
        """Vérifie si toute l’équipe est K.O."""
        return all(p.is_defeated() for p in self.team)
    
    def use_potion(self, pokemon_index=None):
        """Soigne un Pokémon choisi ou un Pokémon aléatoire si rien n’est précisé"""
        if pokemon_index is None:
            # Potion sur un Pokémon encore en vie, choisi au hasard
            available = [p for p in self.team if not p.is_defeated()]
            if not available:
                print(f"{self.name} n’a plus de Pokémon à soigner !")
                return
            target = random.choice(available)
        else:
            target = self.team[pokemon_index]

        target.heal()
        print(f"{self.name} utilise une potion sur {target.name} !")