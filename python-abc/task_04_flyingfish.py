class Fish:
    """
    A class representing a generic fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints the typical habitat of a fish.
    """

    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of a fish.
        """
        print("The fish lives in water")

class Bird:
    """
    A class representing a generic bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints the typical habitat of a bird.
    """

    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of a bird.
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, combining traits from both Fish and Bird.

    Overrides methods from both parent classes to reflect its unique nature.
    """

    def fly(self):
        """
        Print a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print the unique habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")

print(FlyingFish.mro())
