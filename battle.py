from characters import Pokemon, choose_pokemon, enemy_choosing
import random


class Battle:
    def __init__(self):
        player_index = choose_pokemon()
        player_pokemon, enemy_pokemon = enemy_choosing(player_index)
        self.player = player_pokemon
        self.enemy = enemy_pokemon

     
    def choose_action(self):
        while True:
            print(self.player.name, "que veux-tu faire ?")
            print("1) Attaquer")
            print("2) Potion")
            print("3) Passer le tour")
            choice = input(" Choisis un numero : ")
            if choice == "1":
                return "Attaquer"
                 
            elif choice == "2":
                self.player.heal()
                return "Potion"
            
            elif choice == "3":
                return "Passer le tour"
                 
            else:
                print("Entrée invalide ! Choisi 1, 2 ou 3.")   


    def playing(self, action, target):
        print(action)
        if action == "Attaquer":
            target.take_damage(target.get_attack())
            print(target.hp)
        elif action == "Potion":
            self.player.heal()
        elif action == "Passer le tour":
            print(f"{self.player.name} ne fait rien ce tour-ci...")
            

    def enemy_action(self):
        action = random.choice(["Attaquer", "Potion", "Passer le tour"])
        if action == "Attaquer":
            self.enemy.attack_target(self.player)
        elif action == "Potion":
            self.enemy.heal()
        elif action == "Passer le tour":
            print(f"{self.enemy.name} ne fait rien ce tour-ci...")

    def player_hp(self):
            if self.player.hp <= 0:
                print(f"💀 {self.player.name} est K.O. ! Tu as perdu !")
                return True   # le joueur est mort
            return False      # le joueur est encore vivant
        
    def enemy_hp(self):
            if self.enemy.hp <= 0:
                print(f"💀 {self.enemy.name} est vaincu ! Tu as gagné !")
                return True   # l'ennemi est mort
            return False      # il est encore vivant

    def start_battle(self):  
        
        
        while True:
            # --- Tour du joueur ---
            print("--- Tour du joueur ---")
            print(f"{self.player.name} : {self.player.hp}/{self.player.max_hp} PV")
            print(f"{self.enemy.name} : {self.enemy.hp}/{self.enemy.max_hp} PV")
            action = self.choose_action()
            self.playing(action, self.enemy)

            # Vérifie si l'adversaire est K.O.
            if self.enemy.hp <= 0:
                print(f"💀 {self.enemy.name} est vaincu ! Tu as gagné !")
                break

            # --- Tour de l'adversaire ---
            print("--- Tour de l'adversaire ---")
            print(f"{self.player.name} : {self.player.hp}/{self.player.max_hp} PV")
            print(f"{self.enemy.name} : {self.enemy.hp}/{self.enemy.max_hp} PV")

            # --- Tour de l’ennemi ---
            self.enemy_action()

            # Vérifie si le joueur est K.O.
            if self.player.hp <= 0:
                print(f"💀 {self.player.name} est K.O. ! Tu as perdu !")
                break
            
        
        
