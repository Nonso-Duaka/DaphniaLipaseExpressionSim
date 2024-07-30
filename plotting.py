'''import seaborn as sns
import matplotlib.pyplot as plt

def plot_results(time_steps, activity):
    # Check if lengths match
    
    if len(time_steps) != len(activity):
        print("Error: Lengths of time_steps and activity do not match.")
        return

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 1, 1)
    sns.lineplot(x=time_steps, y=activity, label='Lipase/Esterase Activity')
    plt.legend()

    plt.xlabel('Time (hours)')
    plt.ylabel('Activity')
    plt.tight_layout()
    plt.show()'''

import seaborn as sns
import matplotlib.pyplot as plt


def plot_results(time_steps, activity):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 1, 1)
    sns.lineplot(x=time_steps, y=activity, label='Lipase/Esterase Activity')
    plt.legend()

    plt.xlabel('Time (hours)')
    plt.ylabel('Activity')
    plt.tight_layout()
    plt.show()



