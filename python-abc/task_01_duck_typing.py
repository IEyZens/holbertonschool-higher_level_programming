from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Defines the interface that all shapes must implement,
    including methods to compute area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class implementing the Shape interface.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area (π * r^2).
        """
        return self.radius * self.radius * math.pi

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter (2 * π * r).
        """
        return (self.radius * 2) * math.pi


class Rectangle(Shape):
    """
    Rectangle shape class implementing the Shape interface.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter (2 * (width + height)).
        """
        return (self.__width + self.__height) * 2


def shape_info(obj):
    """
    Print the area and perimeter of a shape.

    Uses duck typing: any object with 'area' and 'perimeter' methods is
    accepted.

    Args:
        obj (object): An instance of a shape with 'area' and 'perimeter'
        methods.
    """
    print("Area: ", obj.area())
    print("Perimeter: ", obj.perimeter())
