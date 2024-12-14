"""
app.py

This script contains basic math functions for addition and subtraction.
"""

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first number.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of subtracting b from a.
    """
    return a - b

if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 3))
