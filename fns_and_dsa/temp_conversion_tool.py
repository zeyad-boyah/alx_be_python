FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    # (32°F − 32) × 5/9 = 0°C
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    # (0°C × 9/5) + 32 = 32°F
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    temp = float(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if temp_type == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    elif temp_type == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    else:
        print("Please provide a valid Temperature unit")

main()
