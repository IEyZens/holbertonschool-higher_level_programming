#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    # Class variable to keep track of the number of instances
    number_of_instances = 0
    # Class variable to define the symbol used to print the rectangle
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Set the width of the rectangle
        self.width = width
        # Set the height of the rectangle
        self.height = height
        # Increment the number of instances
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Return the width of the rectangle
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        # Check if value is an integer
        if not isinstance(value, int):
            # raise an exception if value is not an integer
            raise TypeError("width must be an integer")
        # Check if value is less than 0
        if value < 0:
            # raise an exception if value is less than 0
            raise ValueError("width must be >= 0")
        # Set the width of the rectangle
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Return the height of the rectangle
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        # Check if value is an integer
        if not isinstance(value, int):
            # raise an exception if value is not an integer
            raise TypeError("height must be an integer")
        # Check if value is less than 0
        if value < 0:
            # raise an exception if value is less than 0
            raise ValueError("height must be >= 0")
        # Set the height of the rectangle
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        # Calculate the area of the rectangle
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        # Check if width or height is 0
        if self.width == 0 or self.height == 0:
            # If either width or height is 0, return 0
            return 0
        # Calculate the perimeter of the rectangle
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        # Check if width or height is 0
        if self.width == 0 or self.height == 0:
            # If either width or height is 0, return an empty string
            return ""
        # Create a string representation of the rectangle
        else:
            # Create a list to hold the string representation
            new_list = []
            # Append the string representation of the rectangle to the list
            for _ in range(self.height):
                # Append the string representation of the rectangle to the list
                new_list.append(str(self.print_symbol) * self.width)
            # Join the list into a single string with new lines
            # and return the string
            return "\n".join(new_list)

    def __repr__(self):
        """Return a string representation of the rectangle for debugging."""
        # Return a string representation of the rectangle for debugging
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        # Print a message when the rectangle is deleted
        print("Bye rectangle...")
        # Decrement the number of instances
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area."""
        # Check if rect_1 and rect_2 are instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            # raise an exception if rect_1 is not an instance of Rectangle
            raise TypeError("rect_1 must be an instance of Rectangle")
        # Check if rect_2 is an instance of Rectangle
        if not isinstance(rect_2, Rectangle):
            # raise an exception if rect_2 is not an instance of Rectangle
            raise TypeError("rect_2 must be an instance of Rectangle")
        # Compare the areas of the two rectangles
        if rect_1.area() >= rect_2.area():
            # If rect_1 has a greater or equal area, return rect_1
            return rect_1
        # If rect_2 has a greater area, return rect_2
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with equal width and height."""
        # Create a new Rectangle instance with equal width and height
        return cls(size, size)
