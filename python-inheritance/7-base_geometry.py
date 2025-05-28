#!/usr/bin/python3
"""
Defines a base class for geometric shapes with methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    Classe de base pour des formes géométriques.
    Cette classe fournit des méthodes pour valider les entiers et
    calculer la surface des formes géométriques.
    """

    def area(self):
        """
        Méthode pour calculer la surface de la forme géométrique.
        Cette méthode doit être implémentée par les sous-classes.
        Raises:
            Exception: Si la méthode n'est pas implémentée dans une sous-classe.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier positif.
        Args:
            name (str): Le nom de la variable à valider.
            value (int): La valeur à valider.
        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` n'est pas supérieur à 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
