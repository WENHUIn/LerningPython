## Display a Celsius-to-Fahrenheit conversion table.
print("Celsius\t\tFahrenheit")
for celsius in range(10, 31, 5):
    fahrenheit = (celsius * (9 / 5)) + 32
    print("{0}\t\t{1:.0f}".format(celsius, fahrenheit))
