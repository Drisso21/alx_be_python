CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Validate numeric input

        # Ask user for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e if str(e) else 'Invalid temperature. Please enter a numeric value.'}")

if __name__ == "__main__":
    main()