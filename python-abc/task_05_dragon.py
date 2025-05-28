class SwimMixin:
    """
    Mixin class that adds swimming capability.

    Intended to be inherited by classes that should be able to swim.
    """

    def swim(self):
        """
        Print a message indicating the creature swims.
        """
        print("The creature swims!")

class FlyMixin:
    """
    Mixin class that adds flying capability.

    Intended to be inherited by classes that should be able to fly.
    """

    def fly(self):
        """
        Print a message indicating the creature flies.
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, capable of both swimming and flying.

    Inherits from SwimMixin and FlyMixin to gain swim and fly methods.
    """

    def roar(self):
        """
        Print a message indicating the dragon roars.
        """
        print("The dragon roars!")

draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
