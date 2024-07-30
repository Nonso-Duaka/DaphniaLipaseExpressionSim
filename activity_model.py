import math

def simulate_activity(initial_activity, food_concentration, duration):
    time_steps = list(range(duration + 1))
    activity_values = []

    for t in time_steps:
        if 0 < food_concentration <= 0.80:
            current_activity = initial_activity * math.exp(0.0042 * t)
        elif 0.80 < food_concentration <= 0.90:
            current_activity = 60 * math.exp(0.0152 * t)
        elif 0.90 < food_concentration <= 0.95:
            current_activity = 65 * math.exp(0.0152 * t)
        elif 0.95 < food_concentration <= 1.00:
            current_activity = 45 * math.exp(0.0127 * t)
        else:
            print("Error: Input out of range")
            return None

        activity_values.append(current_activity)

    return time_steps, activity_values

