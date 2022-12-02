import random


class Hero:
    """
    Écrire une classe Cercle qui aura des atribut:
    nombre point de vie (2d10)
    force d’attaque (1d6)
    force défense (1d6)
    le nom du héros

    des methode suivant:
    faire une attaque. Retourne une valeur de 1d6 plus la force d’attaque
    recevoir des dommages. Accepte en paramètre le nombre de dommages. hp -= dommage - force_defense.
    Avoir une méthode est_vivant qui retourne une booléenne qui est logiquement associée au nom de la méthode.


    """

    def __init__(self, nom):
        self.nom = nom
        self.hp = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_deffence = random.randint(1, 6)

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


hero1 = Hero("Luc")

hero1.endommage(10)

if hero1.is_alive():
    print("vivant")
else:
    print("RIP")
