from bonus2 import TrainerType, Pokemon_characters_type
from battlebonus2 import BattleBonus2
import random

# Création du joueur
player = TrainerType("Joueur")
player.create_team()
player.choose_active_pokemon()

# Création de l’adversaire
enemy = TrainerType("Adversaire")
enemy.team = random.sample(Pokemon_characters_type, 3)
enemy.active_pokemon = random.choice(enemy.team)

battle = BattleBonus2(player, enemy)
battle.start_battle()