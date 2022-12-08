"""
Zi-jun Zhou Gr:406
"""
import random


class Personnage:
    """
    une dataclass pour prendre en charge les caractéristiques d'un personnage de D&D.
    atttribut: force, dextérité, constitution, intelligence, sagesse et charisme.
    Chaque attribut est initialisé à une valeur aléatoire entre 1 et 20.

    """
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


personnage = Personnage()
print(personnage.force)