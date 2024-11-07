def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp + 460

    tempInCelsius = float(input("ENTER THE TEMPERATURE IN CELCIUS: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    convert = FahrenheitToCelsius(tempInCelsius)
    print(str(convert.conversion()) + " Celsius")

    convert = KelvinToCelsius(tempInCelsius)
    print(str(convert.conversion()) + " Celsius")

main()