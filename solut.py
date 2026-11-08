#Fahrenheit = Celsius × 9 / 5 + 32
"""Převede teplotu ze stupňů Celsia na Fahrenheit.
    
    Args:
        celsius: teplota ve stupních Celsia (číslo)
    
    Returns:
        teplota ve stupních Fahrenheita (číslo)
    """
celsia = float(input("zadej stupně Celsia"))


fahrenheit = round(celsia * 9 / 5 + 32, 2)

print (fahrenheit)




#C = (F - 32) * 5 / 9
def fahrenheit_to_celsius(fahrenheit):
    """Převede teplotu ze stupňů Fahrenheita na Celsius.
    
    Args:
        fahrenheit: teplota ve Fahrenheitech (číslo)
    
    Returns:
        teplota v Celsiích (číslo)
    """
fahrenheit2 = float(input("zadej stupně Fahrenheita"))

Celsia2 = round((fahrenheit2 - 32) * 5 / 9, 2)

print (Celsia2)
