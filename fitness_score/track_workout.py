import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_results():
    data = pd.read_csv('inputs/input_workouts.csv')
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=data)

    plt.title('Track workouts')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')

    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('results/track_workout.png', dpi=300)

plot_results()
