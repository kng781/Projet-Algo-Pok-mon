from characters import Pokemon, choose_pokemon, enemy_choosing
from battle import Battle

while True:
    battle = Battle()
    battle.start_battle()

    choice = input("\nVeux-tu rejouer ? (o/n) : ").lower()
    if choice == "n":
        print("Merci d'avoir joué !")
        break