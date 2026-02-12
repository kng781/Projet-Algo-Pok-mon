import random

class BattleBonus:
    def __init__(self, player_trainer, enemy_trainer):
        self.player_trainer = player_trainer
        self.enemy_trainer = enemy_trainer
        self.player = player_trainer.active_pokemon
        self.enemy = enemy_trainer.active_pokemon

    def choose_action(self):
        """Demande au joueur quelle action il veut faire."""
        while True:
            print(f"\n--- Tour de {self.player_trainer.name} ---")
            print(f"{self.player.name} : {self.player.hp}/{self.player.max_hp} PV")
            print(f"{self.enemy.name} : {self.enemy.hp}/{self.enemy.max_hp} PV")
            print("1) Attaquer")
            print("2) Potion")
            print("3) Changer de Pokémon")
            print("4) Passer le tour")
            choice = input("Choisis un numéro : ")

            if choice == "1":
                return "Attaquer"
            elif choice == "2":
                return "Potion"
            elif choice == "3":
                return "Changer"
            elif choice == "4":
                return "Passer"
            else:
                print("Entrée invalide ! Choisis 1, 2, 3 ou 4.")

    def play_turn(self, action, trainer, target_trainer):
        """Exécute l'action choisie par un dresseur."""
        if action == "Attaquer":
            target = target_trainer.active_pokemon
            damage = trainer.active_pokemon.get_attack()
            target.take_damage(damage)
            print(f"{trainer.active_pokemon.name} attaque {target.name} et inflige {damage} dégâts !")
        elif action == "Potion":
            trainer.use_potion()
        elif action == "Changer":
            trainer.choose_active_pokemon()
        elif action == "Passer":
            print(f"{trainer.name} ne fait rien ce tour-ci...")

    def enemy_turn(self):
        if self.enemy_trainer.all_defeated():
            return
        action = random.choice(["Attaquer", "Potion", "Changer", "Passer"])
        self.play_turn(action, self.enemy_trainer, self.player_trainer)

    def update_active_pokemons(self):
        if self.player.is_defeated():
            print(f"{self.player.name} est K.O. !")
            if not self.player_trainer.all_defeated():
                self.player_trainer.choose_active_pokemon()
            self.player = self.player_trainer.active_pokemon

        if self.enemy.is_defeated():
            print(f"{self.enemy.name} est K.O. !")
            if not self.enemy_trainer.all_defeated():
                self.enemy_trainer.active_pokemon = random.choice(
                    [p for p in self.enemy_trainer.team if not p.is_defeated()]
                )
            self.enemy = self.enemy_trainer.active_pokemon

    def start_battle(self):
        """Boucle principale du combat."""
        while True:
            # Tour du joueur
            action = self.choose_action()
            self.play_turn(action, self.player_trainer, self.enemy_trainer)
            self.update_active_pokemons()

            # Vérifie fin du combat
            if self.player_trainer.all_defeated():
                print(f"\n💀 {self.player_trainer.name} a perdu !")
                break
            if self.enemy_trainer.all_defeated():
                print(f"\n💀 {self.enemy_trainer.name} a perdu !")
                break

            # Tour de l'ennemi
            print(f"\n--- Tour de {self.enemy_trainer.name} ---")
            self.enemy_turn()
            self.update_active_pokemons()

            # Vérifie fin du combat
            if self.player_trainer.all_defeated():
                print(f"\n💀 {self.player_trainer.name} a perdu !")
                break
            if self.enemy_trainer.all_defeated():
                print(f"\n💀 {self.enemy_trainer.name} a perdu !")
                break