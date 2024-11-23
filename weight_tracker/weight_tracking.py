import pandas as pd
import matplotlib.pyplot as plt

# Make dataframe
df = pd.read_csv('Renpho Health.csv')
df['Date'] = pd.to_datetime(df['Time of Measurement'])
df = df.sort_values('Date')

# Plot chart
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df[' Weight(kg)'], marker= 'o')
plt.title('My Weight Over Time', fontsize=12)
plt.xlabel('Date')
plt.ylabel('Weight (kg)')
plt.grid(True, linestyle = '--', alpha = 0.7)
plt.savefig('weight_tracking_chart.png', dpi=300, bbox_inches='tight')
plt.close()