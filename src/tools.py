from transformers import tool

@tool
def add_numbers(a:float, b:float) -> float:
    """
    This tool takes two floating point numbers as input, and returns their sum.

    Args:
        a: The first number
        b: The second number
    """
    return a+b

@tool
def raise_to_power(base:float, power:float) -> float:
    """
    This tool takes two floating point number inputs, and calculates the base input raised to the power input.

    Args:
        base: The number to raise
        power: The power to raise the base to
    """
    return base**power

@tool
def subtract_numbers(a: float, b: float) -> float:
    """
    This tool takes two floating point numbers as input and returns their difference.

    Args:
        a: The first number
        b: The second number
    """
    return a - b

@tool
def multiply_numbers(a: float, b: float) -> float:
    """
    This tool takes two floating point numbers as input and returns their product.

    Args:
        a: The first number
        b: The second number
    """
    return a * b

@tool
def divide_numbers(a: float, b: float) -> float:
    """
    This tool takes two floating point numbers as input and returns the result of dividing the first by the second.

    Args:
        a: The numerator
        b: The denominator

    Raises:
        ValueError: If the denominator is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def calculate_modulus(a: float, b: float) -> float:
    """
    This tool takes two floating point numbers as input and returns the modulus of the first number by the second.

    Args:
        a: The first number
        b: The second number

    Raises:
        ValueError: If the denominator is zero
    """
    if b == 0:
        raise ValueError("Cannot calculate modulus with a denominator of zero.")
    return a % b
