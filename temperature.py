temperature = float(input("celsius"))

# převod na kelviny a farrenheita
fahrenheit = round(temperature* 9 / 5 + 32, 2)
kelvin = round(temperature + 273.15, 2)

# print
print(f"{temperature} °C = {fahrenheit} °F = {kelvin} K")