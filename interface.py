def get_user_input():

    
    initial_activity = float(input("Enter initial lipase/esterase activity (in µmol/min/mg protein): "))
    
    is_lipid_rich_food = input("Is the food lipid-rich? (yes/no): ").lower() == "no"
    
    if is_lipid_rich_food:
        food_concentration = float(input("Enter food concentration (in µM, range: 0 to 1 mgC per litre): "))
        while not (0 <= food_concentration <= 1):
            print("Invalid input. Concentration must be in the range of 0 to 1 mgC per litre.")
            food_concentration = float(input("Enter food concentration (in µM, range: 0 to 1 mgC per litre): "))
    else:
        food_concentration = None
    
    duration = int(input("Enter simulation duration (in hours, up to 144): "))
    if duration > 144:
        print("Duration has been restricted to a maximum of 144 hours.")
        duration = 144

    return initial_activity, is_lipid_rich_food, food_concentration, duration


def display_results( final_activity):
    print(f"The final lipase/esterase activity is: {final_activity} µmol/min/mg protein")

