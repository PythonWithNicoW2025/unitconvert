"""
This module provides functions to convert weight units.
Demonstrates Google Python Style Guide section on functions.
"""


def kg_to_pounds(kg):
    """
    Convert weight from kilograms to pounds.

    Args:
        kg (float): Weight in kilograms

    Returns:
        float: Weight in pounds

    Raises:
        ValueError: If input is not numeric
    """
    if not isinstance(kg, (int, float)):
        raise ValueError("Input must be numeric")
    return kg * 2.20462


def pounds_to_kg(pounds):
    """"
    Convert weight from pounds to kilograms.

    Args:
        pounds (float): Weight in pounds

    Returns:
        float: Weight in kilograms

    Raises:
        ValueError: If input is not numeric
    """
    if not isinstance(pounds, (int, float)):
        raise ValueError("Input must be numeric")
    return pounds / 2.20462
