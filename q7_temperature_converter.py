# ============================================================
# Question 7: Temperature Converter
# Difficulty: Medium | Points: 4
# Description: Menu-driven temperature converter with 6 options
# ============================================================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit: (C × 9/5) + 32"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius: (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin: C + 273.15"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius: K - 273.15"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15"""
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32"""
    return (kelvin - 273.15) * 9 / 5 + 32

# ── Main menu loop ────────────────────────────────────────────
print("=== TEMPERATURE CONVERTER ===")

while True:
    # Display the menu
    print("\n1. Celsius    → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius    → Kelvin")
    print("4. Kelvin     → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin     → Fahrenheit")
    print("7. Exit")

    try:
        choice = int(input("\nEnter your choice (1-7): "))

        if choice == 7:
            print("Goodbye! Stay warm! 🌡️")
            break

        elif choice in (1, 2, 3, 4, 5, 6):
            # Map choice to: (label, unit, conversion function)
            options = {
                1: ("Celsius",    "°C", celsius_to_fahrenheit,  "Fahrenheit", "°F"),
                2: ("Fahrenheit", "°F", fahrenheit_to_celsius,  "Celsius",    "°C"),
                3: ("Celsius",    "°C", celsius_to_kelvin,      "Kelvin",     "K"),
                4: ("Kelvin",     "K",  kelvin_to_celsius,      "Celsius",    "°C"),
                5: ("Fahrenheit", "°F", fahrenheit_to_kelvin,   "Kelvin",     "K"),
                6: ("Kelvin",     "K",  kelvin_to_fahrenheit,   "Fahrenheit", "°F"),
            }
            from_unit_name, from_symbol, convert_fn, to_unit_name, to_symbol = options[choice]

            temperature_input = float(input(f"Enter temperature in {from_unit_name} ({from_symbol}): "))

            # Edge case: Kelvin cannot be negative
            if from_unit_name == "Kelvin" and temperature_input < 0:
                print("Error: Kelvin temperature cannot be negative (Absolute Zero = 0 K).")
                continue

            converted_temperature = convert_fn(temperature_input)
            print(f"\nResult: {temperature_input}{from_symbol} = {converted_temperature:.2f}{to_symbol}")

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("Error: Please enter a valid number.")
