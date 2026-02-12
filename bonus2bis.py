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