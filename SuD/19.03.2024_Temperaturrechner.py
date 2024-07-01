def main():
    while True:
        print("""   1: Celsius zu Fahrenheit
                    2: Fahrenheit zu Celsius
                    3: Celsius zu Kelvin
                    4: Kelvin zu Celsius
                    0: Programm beenden""")

        match int(input()):
            case 1:
                print(CelsiusToFahrenheit(float(input("Bitte gebe die Celsius Temperatur an:\n"))))
            case 2:
                print(FahrenheitToCelsius(float(input("Bitte gebe die Fahrenheit Temperatur an:\n"))))
            case 3:
                print(CelsiusToKelvin(float(input("Bitte gebe die Celsius Temperatur an:\n"))))
            case 4:
                print(KelvinToCelsius(float(input("Bitte gebe die Kelvin Temperatur an:\n"))))
            case 0:
                break


def CelsiusToFahrenheit(value):
    return float(value * 9 / 5 + 32)


def FahrenheitToCelsius(value):
    return float((value - 32) * 5 / 9)


def CelsiusToKelvin(value):
    return float(value + 273.15)


def KelvinToCelsius(value):
    return float(value - 273.15)


if __name__ == "__main__":
    main()
