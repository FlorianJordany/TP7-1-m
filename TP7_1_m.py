class Parallelepipede:
    def __init__(self, longueur=10, largeur=6, hauteur=8):
        self.nom = 'parallelepipede'
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def volume(self):
        return self.longueur * self.largeur * self.hauteur

    def __str__(self):
        return f"Le {self.nom} de côtés {self.longueur}, {self.largeur} et {self.hauteur} a un volume de {self.volume()}"

if __name__ == '__main__':
    parallelepipede = Parallelepipede(12, 8, 10)
    print(parallelepipede)

class Cube(Parallelepipede):
    def __init__(self, cote=10):
        super().__init__(cote, cote, cote)
        self.nom = 'cube'

if __name__ == '__main__':
    cube = Cube(10)
    print(cube)
