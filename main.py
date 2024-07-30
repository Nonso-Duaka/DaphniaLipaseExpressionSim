

import interface
import activity_model
import plotting
import gene_expression_model  # Assuming this is the correct name of your module

def main():
    # Get user input
    initial_activity, is_lipid_rich_food, food_concentration, duration = interface.get_user_input()

    gene_expression_model.analyze_gene_expression(food_concentration, duration)

    time_steps, final_activity = activity_model.simulate_activity(initial_activity, food_concentration, duration)
    interface.display_results(final_activity)

    # Visualize results
    time_steps = list(range(duration + 1))  # Time steps from 0 to duration
    plotting.plot_results(time_steps, final_activity)

if __name__ == "__main__":
    main()


