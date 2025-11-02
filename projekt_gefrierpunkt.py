frozen_water = 0
frozen_ethanol = -114.5
frozen_benzin = -60

gas_water = 100
gas_ethanol = 78.3
gas_benzin = 30

user_input = input("Gib eine Temparatur ein in Celsius: ")

def check_state(temp, freezing_point, boiling_point):
    if temp <= freezing_point:
        return "fest"
    elif temp >= boiling_point:
        return "gasförmig"
    else:
        return "flüssig"


def print_state(substance, state, temp):
    print("Bei " + str(temp) + "°C ist " + substance + " " + state)

def main(input):
    try:
        number = float(input)
        state_of_water = check_state(number, frozen_water, gas_water)
        state_of_ethanol = check_state(number, frozen_ethanol, gas_ethanol)
        state_of_benzin = check_state(number, frozen_benzin, gas_benzin)

        print_state("Wasser", state_of_water, number)
        print_state("Ethanol", state_of_ethanol, number)
        print_state("Benzin", state_of_benzin, number)


    except:
        print("Bitte eine gültige Zahl eingeben.")

main(user_input)