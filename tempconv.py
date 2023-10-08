def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Conversion Program")
    print("Supported temperature units: Celsius (C), Fahrenheit (F), Kelvin (K)")

    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original temperature unit (C/F/K): ").upper()
    
    celsius = 0  # Initialize celsius variable to 0
    
    if original_unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
    elif original_unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
    elif original_unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid input for original unit. Please use 'C', 'F', or 'K'.")
        return

    print(f"{temperature} {original_unit} is equivalent to:")
    print(f"{fahrenheit:.2f} F")
    print(f"{celsius:.2f} C")
    print(f"{kelvin:.2f} K")

if __name__ == "__main__":
    main()
