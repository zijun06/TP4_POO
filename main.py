"""
Zi-jun Zhou Gr:406
"""


class Rectangle:
    """
    #2
    Écrire une classe Rectangle qui reçoit la largeur ainsi que
    la longueur comme paramètre dans la méthode __init__.
    Écrire une méthode calcul_aire qui permet de calculer l’aire du rectangle
    (elle n’affiche rien à l’écran).
    Écrire aussi une méthode afficher_infos qui permet
    d’afficher les caractéristiques du rectangle.
    """

    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longeur = longueur
        self.air = 0

    def calcul_air(self):
        """
       une méthode calcul_aire qui permet de calculer l’aire du rectangle
       (elle n’affiche rien à l’écran).
       :return:
       """
        self.air = self.largeur * self.longeur

    def afficher_infos(self):
        """
       aussi une méthode afficher_infos qui permet
       d’afficher les caractéristiques du rectangle.
       :return:
       """
        print(f"largeur du rectangle:{self.largeur}\n"
              f"longeur du rectangle:{self.longeur}\n"
              f"Air du rectangle: {self.air}\n")


rectangle_1 = Rectangle(2, 6)

rectangle_1.calcul_air()
rectangle_1.afficher_infos()
