#!/usr/bin/python3
"""Defines the Rectangle class with customizable print_symbol and instance tracking."""

class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize rectangle width and height, increment instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable string representation of the rectangle
        using the symbol(s) stored in print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        line = str(self.print_symbol) * self.__width
        rect_lines = [line for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message and decrement instance count upon deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

