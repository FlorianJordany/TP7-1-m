#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Module de la classe Point.
# fichier : point_m.py
# auteur : Bob Cordeau
# import
from math import hypot
# classe
class Point(object):
# Definit les points de l'espace 2D.
    def __init__(self, x=3.0, y=4.0):
# Constructeur avec valeurs par defaut.
        self.x, self.y = x, y

    def distance(self):
# Retourne la distance euclidienne du point à l'origine.
        return hypot(self.x, self.y)

    def __str__(self):
# Modele d'affichage des attributs d'un Point.
        return "[x = {:g}, y = {:g} ; d = {:g}]" .format(self.x, self.y, self.distance())

# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
    help(Point)
    p = Point()
    print (p)
    p2 = Point(3.7, 8.1)
    print (p2)