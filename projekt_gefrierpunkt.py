frozen_water = 0
frozen_ethanol = -114.5
frozen_benzin = -60

gas_water = 100
gas_ethanol = 78.3
gas_benzin = 30

user_input_water = input("Gib eine Temparatur ein in Celsius für Wasser: ")
user_input_ethanol = input("Gib eine Temparatur ein in Celsius für Ethanol: ")
user_input_benzin = input("Gib eine Temparatur ein in Celsius für Benzin: ")


try:
    number = float(user_input_water)
    if number >= frozen_water and number <= gas_water:
        print("Wasser ist flüssig")
    elif number >= gas_water:
        print("Wasser ist gasförmig")
    else:
        print("Wasser ist gefroren")
except:
    print("not a number")

try:
    number = float(user_input_ethanol)
    if number >= frozen_ethanol and number <= gas_ethanol:
        print("Alkohol ist flüssig")
    elif number >= gas_ethanol:
        print("Alkohol ist gasförmig")
    else:
        print("Alkohol ist gefroren")
except:
    print("not a number")
try:
    number = float(user_input_benzin)
    if number >= frozen_benzin and number <= gas_benzin:
        print("Benzin ist flüssig")
    elif number >= gas_benzin:
        print("Benzin ist gasförmig")
    else:
        print("Benzin ist gefroren")
except:
    print("not a number")