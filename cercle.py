"""
Zi-jun Zhou Gr:406
"""

from math import pi


class Cercle:
    """
    Écrire une classe Cercle qui aura deux méthodes:
    calcul_aire et calcul_circonference.
    Les deux méthodes retournent le résultat du calcul.
    Il faut un attribut pour conserver la valeur du rayon
    """

    def __init__(self, rayon):
        self.rayon = rayon
        self.circonferance = 0.0
        self.aire = 0.0

    def calcul_aire(self):
        """
        calculer l'air du cercle.
        :return:
        """
        self.aire = pi * self.rayon * self.rayon

    def calcul_circonferance(self):
        """
        calculer la circonferance du cercle.
        :return:
        """
        self.circonferance = 2 * pi * self.rayon



cercle = Cercle(55.8)

cercle.calcul_circonferance()
cercle.calcul_aire()

print(f"{cercle.aire}\n"
      f"{cercle.circonferance}")
