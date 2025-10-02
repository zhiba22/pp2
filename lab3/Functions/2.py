#TEMP
def temperature( F):
    C = (5/9) * (F - 32)
    print(f"centigrate temperature = {C}")
user_input = float(input("Temperarure in Fahrenheit: "))  
temperature(user_input)