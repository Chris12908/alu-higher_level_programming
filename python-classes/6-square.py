#!/usr/bin/python3
"""
This module defines the Square class with size and position,
including validation, area calculation, and formatted output.
"""


class Square:
    """
    Represents a square with size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of two non-negative integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#',
        considering the position attribute.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print empty lines (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with leading spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

