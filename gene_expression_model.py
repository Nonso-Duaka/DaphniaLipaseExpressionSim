


def analyze_gene_expression(food_concentration, duration):
    if 0 <= food_concentration <= 1:
        if duration <= 12:
            print("Genes expressed are L34, L29, L33, L50, L35.")
            print("L35 and L29 increased")
            print("Decrease in expressions of L33 and L50 was as a result of the percentage of non-lipid rich foods.")
        elif duration <= 144:
            print("Genes expressed are L34, L29, L33, L50, L35.")
            print("L34 and L29 increased")
            print("Decrease in expressions of L33 and L50 was as a result of the percentage of non-lipid rich foods.")
        else:
            print("Invalid input. Please ensure duration is less than 0 or greater than 144 hours.")
    else:
        print("Invalid input for visualization. Please ensure food concentration is between 0 and 1.")

        
