#GRAMS
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    print(f"ounces = {ounces}")
user_input = float(input("Grams: ")) 
grams_to_ounces(user_input)