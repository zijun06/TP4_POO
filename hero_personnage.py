"""
Zi-jun Zhou Gr:406
"""
import random
from dataclasses import dataclass


@dataclass
class HeroPersonnage:
    """
    la classe écrite à l'exercice #4 et ajouter un attribut basé sur la dataclasse écrite à l'exercice #5.

    """
    nom: str
    hp = random.randint(1, 10) + random.randint(1, 10)
    force_attaque = random.randint(1, 6)
    force_deffence = random.randint(1, 6)
    intelligence: int = random.randint(1, 20)

    def attaque(self):
        """
        faire une attaque. Retourne une valeur de 1d6 plus la force d’attaque
        :return:
        """
        return self.force_attaque + random.randint(1, 6)

    def endommage(self, dommage):
        """
        recevoir des dommages. Accepte en paramètre le nombre de dommages. hp -= dommage - force_defense.

        :param dommage:
        :return:
        """
        self.hp -= dommage - self.force_deffence

    def is_alive(self):
        """
        une méthode est_vivant qui retourne une booléenne qui est logiquement associée au nom de la méthode.
        :return:
        """
        return self.hp > 0


hero1 = HeroPersonnage("Luc")

hero1.endommage(10)

if hero1.is_alive():
    print("vivant")
else:
    print("RIP")
