def main():
    temperature = 0
    converted_temperature = 0
    valid_temperature = False
    while not valid_temperature:
        try:
            temperature = int(input("Please enter the temperature for conversion: "))
            valid_temperature = True
        except ValueError:
            print("Invalid Entry")
    valid_temperature_type = False
    while not valid_temperature_type:
        try:
            temperature_type = input("Was that (C)elsius or (F)ahrenheit? ")
            if temperature_type.upper() == "F":
                converted_temperature = calc_fahrenheit_to_celsius(temperature)
                valid_temperature_type = True
            elif temperature_type.upper() == "C":
                converted_temperature = calc_celsius_to_fahrenheit(temperature)
                valid_temperature_type = True
            else:
                print("Invalid Entry")
        except ValueError:
            print("Invalid Entry")
    print("Converted Temperature =", converted_temperature)


def calc_celsius_to_fahrenheit(temperature):
    return temperature * (9 / 5) + 32


def calc_fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)


main()
