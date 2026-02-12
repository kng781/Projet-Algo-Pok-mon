## Présentation du Projet
Ce projet est un simulateur de combat Pokémon développé en Python, mettant l'accent sur la **Programmation Orientée Objet (POO)**. Il retrace une évolution progressive du code, partant d'un combat simple entre deux entités jusqu'à un système complexe de dresseurs gérant des équipes de Pokémon avec des avantages élémentaires (Types).

## Évolutions du Projet (Versions)

Le projet est découpé en trois étapes majeures reflétées dans les fichiers :

1.  **Version Base (`start.py`) :** Combat 1v1 simple. Choix d'un Pokémon et duel contre l'ordinateur.
2.  **Bonus 1 (`startbonus1.py`) :** Introduction de la classe `Trainer`. Gestion d'une équipe de 3 Pokémon, possibilité de changer de Pokémon actif en plein combat et système de potions.
3.  **Bonus 2 (`startbonus2.py`) :** Version la plus avancée. Introduction de la classe `PokemonType` (Héritage). Gestion des types (Feu, Eau, Plante) avec multiplicateurs de dégâts.

## Architecture Technique

### Les Classes principales
* **`Pokemon` (`pokemonClass.py`) :** La classe mère. Gère les attributs de base (HP, max_hp, attack_power) et les méthodes universelles (`take_damage`, `heal`, `is_defeated`).
* **`PokemonType` (`bonus2.py`) :** Hérite de `Pokemon`. Ajoute l'attribut `type` et réécrit la méthode `attack_target` pour inclure la logique de faiblesse/résistance.
* **`Trainer` (`bonus1.py`) / `TrainerType` (`bonus2.py`) :** Gère l'humain ou l'IA. Possède une liste de Pokémon et gère le switch entre eux.
* **`Battle` / `BattleBonus2` :** Le moteur qui orchestre les tours de jeu et les conditions de victoire.

### Logique des Types
Le système suit la règle circulaire classique :
* **Feu**  : x2 contre Plante, x0.5 contre Eau.
* **Eau**  : x2 contre Feu, x0.5 contre Plante.
* **Plante**  : x2 contre Eau, x0.5 contre Feu.



## Structure des fichiers

| Fichier | Rôle |
| :--- | :--- |
| `pokemonClass.py` | Définition de la classe mère `Pokemon`. |
| `characters.py` | Liste des Pokémon disponibles et logique de sélection. |
| `battlebonus2.py` | Moteur de combat avancé avec gestion des types et des dresseurs. |
| `bonus2.py` | Classes `PokemonType` et `TrainerType` (Logique métier avancée). |
| `startbonus2.py` | **Point d'entrée principal** de la version complète. |

## Comment lancer le jeu ?

Pour jouer à la version la plus complète (avec types et équipes) :

1. Assurez-vous d'avoir tous les fichiers dans le même dossier.
2. Lancez le script de démarrage via votre terminal :

```bash
python startbonus2.py
