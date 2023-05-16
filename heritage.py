class Mammifere(object):
    def __init__(self) :
        self.caractMam = "il allaite ses petits ;"

class Carnivore(Mammifere):
    def __init__(self) :
        Mammifere.__init__(self)
        self.caractCar = "il se nourrit de la chair de ses proies ;"

class Chien(Carnivore):
    def __init__(self) :
        Carnivore.__init__(self)
        self.caractCh = "son cri se nomme aboiement ;"

# Création des obj
mammifere = Mammifere()
carnivore = Carnivore()
chien = Chien()

# Affichage des attributs
print("Mammifere : ", '\n', mammifere.caractMam)
print("Carnivore : ", '\n', carnivore.caractMam, carnivore.caractCar)
print("Chien : '\n", chien.caractMam, chien.caractCar, chien.caractCh)