#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pytest

# Classe Vector


class Vector (object):

    """
    Classe représentant des vecteurs à deux dimensions. Celle-ci présente
    un constructeur donnant par défaut le point (0,0), ainsi qu'une
    surcharge des opérateurs addition, multiplication par un entier et
    multiplication scalaire entre vecteurs.
    Elle propose également une méthode renvoyant la norme carré du vecteur.
    """

    def __init__(self, x=0, y=0):
        """
        Constructeur de la classe Vector.

        Args:
                x, y: coordonnées du vecteur construit ; par défaut (0,0)
        Raises:
                TypeError si x ou y ne sont pas des nombres.
        """
        raise NotImplementedError("Implémentez Vector.__init__")

    def __str__(self):
        """
        Surcharge de l'opérateur str
        Renvoie "(x, y)" avec une espace après la virgule et 2 décimales
        """
        raise NotImplementedError("Implémentez Vector.__str__")

    def __add__(self, other):
        """
        Opérateur addition entre deux vecteurs.

        Args:
                other: un autre vecteur
        Returns:
                un autre objet Vector représentant la somme de self et other
        """
        raise NotImplementedError("Implémentez Vector.__add__")

    def __sub__(self, other):
        """
        Opérateur soustraction entre deux vecteurs.

        Args:
                other: un autre vecteur
        Returns:
                un autre objet Vector représentant la différence de self et other
        """
        raise NotImplementedError("Implémentez Vector.__sub__")

    def __mul__(self, p=1):
        """
        Opérateur multiplication des composantes par un réel.

        Args:
                p: le réel multiplicateur
        Returns:
                un autre objet Vector représentant self*scal
        """
        raise NotImplementedError("Implémentez Vector.__mul__")

    __rmul__ = __mul__  # multiplication à droite

    def scal(self, other):
        """
        Opérateur produit scalaire entre deux vecteurs.

        Args:
                other: un autre vecteur
        Returns:
                le produit scalaire de self et other
        """
        raise NotImplementedError("Implémentez Vector.scal")

    def norm(self):
        """
        Opérateur norme 2 du vecteur.

        Returns:
                la norme du vecteur.
        """
        raise NotImplementedError("Implémentez Vector.norm")


# tests unitaires fournis pour Vector
# fonction utile pour tester l'égalité sur les réels
def assert_floats(a, b, tol):
    assert(abs(a - b) < abs(tol))


def test_Vector_init():
    tol = 1.e-6
    v = Vector(1, -1)
    assert_floats(v.x, 1, tol)
    assert_floats(v.y, -1, tol)


def test_Vector_str():
    assert(str(Vector(1, -2.653)) == "(1.00, -2.65)")


def test_Vector_add():
    tol = 1.e-6
    v1 = Vector(1, -1)
    v2 = Vector(1, 1)
    assert_floats((v1 + v2).x, 2, tol)
    assert_floats((v1 + v2).y, 0, tol)


def test_Vector_sub():
    tol = 1.e-6
    v1 = Vector(1, -1)
    v2 = Vector(1, 1)
    assert_floats((v1 - v2).x, 0, tol)
    assert_floats((v1 - v2).y, -2, tol)


def test_Vector_mul():
    tol = 1.e-6
    r = 2
    v = Vector(1, -1)
    assert_floats((r * v).x, 2, tol)
    assert_floats((v * r).y, -2, tol)


def test_Vector_scal():
    tol = 1.e-6
    v1 = Vector(1, -1)
    v2 = Vector(2, 1)
    assert_floats(v1.scal(v2), 1, tol)
    assert_floats(v2.scal(v1), 1, tol)


def test_Vector_norm():
    tol = 1.e-6
    v1 = Vector(1, -1)
    assert_floats(v1.norm(), 2 ** 0.5, tol)


# Classe Simulation
class Simulation (object):

    """
    Classe représentant une simulation de chute libre d'un point matériel
    de masse m et à coefficient de frottements et vitesse initiale donnés.
    """

    def __init__(self, m, k, v0, dt):
        """
        Constructeur de la classe Simulation. Fixe la masse du système,
        la vitesse initiale, le coefficient de frottements et le pas de temps.

        Args:
                m: la masse du système
                k: le coefficient de frottements
                v0: la vitesse initiale
                dt: le pas de temps
        Raises:
                TypeError si m, k ou dt ne sont pas des réels,
                        ou si v0 n'est pas un Vector
                ValueError si m est négatif ou nul, si k n'est pas compris
                        entre 0 et 1, si v0.x ou v0.y est négatif ou nul, si dt
                        est négatif ou nul
        """
        raise NotImplementedError("Implémentez Simulation.__init__")

    def step(self):
        """
        Calcule un pas de temps et l'ajoute à l'historique.
        """
        raise NotImplementedError("Implémentez Simulation.step")

    def run(self):
        """
        Calcule le mouvement complet.
        """
        raise NotImplementedError("Implémentez Simulation.run")

    def maxDistance(self):
        """
        Renvoie la distance maximale atteinte par le point matériel avant
        de retoucher le sol.
        """
        raise NotImplementedError("Implémentez Simulation.maxDistance")

    def maxAltitude(self):
        """
        Renvoie l'altitude maximale atteinte par le point matériel au cours
        de la trajectoire.
        """
        raise NotImplementedError("Implémentez Simulation.maxAltitude")

    def finalSpeed(self):
        """
        Renvoie un vecteur correspondant à la vitesse en fin de trajectoire.
        """
        raise NotImplementedError("Implémentez Simulation.finalSpeed")

    def energy(self):
        """
        Calcule et renvoie l'historique de l'énergie mécanique au cours
        du mouvement.
        """
        raise NotImplementedError("Implémentez Simulation.energy")


# tests unitaires fournis pour Simulation
def test_Simulation_init():
    tol = 1.e-6
    s = Simulation(1, 0.5, Vector(1, 1), 0.01)
    assert_floats(s.m, 1, tol)
    assert_floats(s.k, 0.5, tol)
    assert_floats(s.r[0].x, 0, tol)
    assert_floats(s.r[0].y, 0, tol)
    assert_floats(s.v[0].x, 1, tol)
    assert_floats(s.v[0].y, 1, tol)


def test_Simulation_step():
    tol = 1.e-6
    s = Simulation(1, 0., Vector(1, 10), 1.)
    s.step()
    assert_floats(s.r[-1].x, 1, tol)
    assert_floats(s.r[-1].y, 10, tol)
    assert_floats(s.v[-1].x, 1, tol)
    assert_floats(s.v[-1].y, 0.2, tol)


def test_Simulation_run():
    tol = 1.e-2
    s = Simulation(1, 0., Vector(1, 1), 1.e-3)
    s.run()
    assert(s.r[-1].y < 0)
    assert(s.r[-2].y > 0)
    assert_floats(s.r[-1].x, 2 / 9.8, tol)


def test_Simulation_maxDistance():
    tol = 1.e-2
    s = Simulation(1, 0., Vector(1, 1), 1.e-3)
    s.run()
    assert_floats(s.maxDistance(), 2 / 9.8, tol)


def test_Simulation_maxAltitude():
    tol = 1.e-2
    s = Simulation(1, 0., Vector(1, 1), 1.e-3)
    s.run()
    assert_floats(s.maxAltitude(), 0.5 / 9.8, tol)


def test_Simulation_finalSpeed():
    tol = 1.e-2
    s = Simulation(1, 0., Vector(1, 1), 1.e-4)
    s.run()
    v = s.finalSpeed()
    assert_floats(v.x, 1, tol)
    assert_floats(v.y, -1, tol)


def test_Simulation_energy():
    tol = 1.e-2
    s = Simulation(1, 0., Vector(1, 1), 1.e-3)
    s.run()
    en = s.energy()
    assert_floats(en[0], 1, tol)
    assert_floats(en[-1], 1, tol)
