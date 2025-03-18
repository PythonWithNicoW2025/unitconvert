"""
CLI for the unitconvert package
"""
from unitconvert.temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)
from unitconvert.length import inches_to_cm, cm_to_inches
from unitconvert.weight import kg_to_pounds, pounds_to_kg


def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit
    """
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        value = float(input("Enter temperature in Celsius: "))
        print(f"{value}°C = {celsius_to_fahrenheit(value)}°F")
    elif choice == "2":
        value = float(input("Enter temperature in Fahrenheit: "))
        print(f"{value}°F = {fahrenheit_to_celsius(value)}°C")
    else:
        print("Invalid choice.")


def convert_length():
    """
    Convert length between inches and centimeters
    """
    print("\nLength Conversion")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        value = float(input("Enter length in inches: "))
        print(f"{value} inches = {inches_to_cm(value)} cm")
    elif choice == "2":
        value = float(input("Enter length in centimeters: "))
        print(f"{value} cm = {cm_to_inches(value)} inches")
    else:
        print("Invalid choice.")


def convert_weight():
    """
    Convert weight between kilograms and pounds"
    """
    print("\nWeight Conversion")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        value = float(input("Enter weight in kilograms: "))
        print(f"{value} kg = {kg_to_pounds(value)} lb")
    elif choice == "2":
        value = float(input("Enter weight in pounds: "))
        print(f"{value} lb = {pounds_to_kg(value)} kg")
    else:
        print("Invalid choice.")


def main():
    """
    Main function for the CLI
    """
    while True:
        print("\n🔹 Unit Conversion Menu 🔹")
        print("1. Convert Temperature")
        print("2. Convert Length")
        print("3. Convert Weight")
        print("4. Exit")
        
        option = input("Choose a category (1-4): ")

        if option == "1":
            convert_temperature()
        elif option == "2":
            convert_length()
        elif option == "3":
            convert_weight()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
