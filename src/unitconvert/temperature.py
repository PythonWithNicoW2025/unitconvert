"""
This module provides functions to convert temperature units.
"""


def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    if not isinstance(c, (int, float)):
        raise ValueError("Input must be numeric")
    return c * 9/5 + 32


def fahrenheit_to_celsius(f):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        f (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    if not isinstance(f, (int, float)):
        raise ValueError("Input must be numeric")
    return (f - 32) * 5/9
