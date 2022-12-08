"""
Zi-jun Zhou Gr:406
"""


class StringFoo:
    """
   # 1
   Écrire une classe StringFoo qui contient:
   un attribut message;
   une méthode set_string
   accepte une string en paramètre et la sauvegarde dans l'attribut message.
   une méthode print_string
   affiche le contenu de l'attribut message tout en majuscule.
   """

    def __init__(self):
        self.message = ""

    def set_string(self):
        """
       accepte une string en paramètre et la sauvegarde dans l'attribut message.
       :return:
       """
        self.message = str(input("Entrer le message:_"))

    def print_string(self):
        """
       affiche le contenu de l'attribut message tout en majuscule.
       :return:
       """
        print(self.message.upper())


stringfoo_1 = StringFoo()

stringfoo_1.set_string()
stringfoo_1.print_string()
