from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class enforces the implementation of the 'sound' method
    in any subclass, ensuring each animal can produce a sound.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Implements the sound method to return the sound a dog makes.
    """

    def sound(self):
        """
        Returns the sound made by a dog.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Implements the sound method to return the sound a cat makes.
    """

    def sound(self):
        """
        Returns the sound made by a cat.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
