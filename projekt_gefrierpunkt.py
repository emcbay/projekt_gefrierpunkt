frozen_water = 0
frozen_ethanol = -114.5
frozen_benzin = -60

gas_water = 100
gas_ethanol = 78.3
gas_benzin = 30

# liquid_water = 
# liquid_ethanol = 
# liquid_benzin = 

user_input = input("Gib eine Temparatur ein in Celsius: ")
# if type(int(user_input)) or type(float(user_input)):
#     print(user_input)
# else:
#     print("Keine Zahl")

try:
    number = float(user_input)
    if number >= frozen_water and number <= gas_water
    print()
except:
    print("not a number")