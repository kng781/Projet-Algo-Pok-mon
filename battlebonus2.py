import random

class BattleBonus2:
    def __init__(self, player_trainer, enemy_trainer):
        self.player_trainer = player_trainer
        self.enemy_trainer = enemy_trainer
        self.player = player_trainer.active_pokemon
        self.enemy = enemy_trainer.active_pokemon

    def start_battle(self):
        while True:
            # Tour joueur
            print(f"\n--- Tour de {self.player_trainer.name} ---")
            print(f"{self.player.name} ({self.player.type}) : {self.player.hp}/{self.player.max_hp} PV")
            print(f"{self.enemy.name} ({self.enemy.type}) : {self.enemy.hp}/{self.enemy.max_hp} PV")
            action = input("1) Attaquer 2) Potion 3) Changer : ")
            if action == "1":
                self.player.attack_target(self.enemy)
            elif action == "2":
                self.player.heal()
            elif action == "3":
                self.player_trainer.choose_active_pokemon()
                self.player = self.player_trainer.active_pokemon

            if self.enemy.hp <= 0:
                print(f"{self.enemy.name} est K.O. ! Tu as gagné !")
                break

            # Tour adversaire
            action_enemy = random.choice(["attaque", "potion"])
            if action_enemy == "attaque":
                self.enemy.attack_target(self.player)
            else:
                self.enemy_trainer.active_pokemon.heal()
            if self.player.hp <= 0:
                print(f"{self.player.name} est K.O. ! Tu as perdu !")
                break