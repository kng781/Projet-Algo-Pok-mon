from characters import Pokemon_characters
from bonus1 import Trainer                
from battlebonus1 import BattleBonus
import random


# Création du joueur
player_trainer = Trainer(name="Joueur")
player_trainer.create_team()
player_trainer.choose_active_pokemon()

# Création de l’adversaire
enemy_team = random.sample(Pokemon_characters, 3)
enemy_trainer = Trainer(name="Adversaire")
enemy_trainer.team = enemy_team
enemy_trainer.active_pokemon = random.choice(enemy_team)
        


battle = BattleBonus(player_trainer, enemy_trainer)
battle.start_battle()  # lance le combat
