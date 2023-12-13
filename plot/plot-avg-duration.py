import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from db.get_alarms import get_alarms

# Assuming get_alarms returns a list of objects with attributes date, alarmend, and oblast
alarms = get_alarms()

# Create a list to store data for the CSV file
data = []
i = 0
for alarm in alarms:
    start_date = alarm.date
    end_date = alarm.alarmend.date
    oblast = alarm.oblast
    i += 1
    if i == 10:
        break
    # Append data to the list
    data.append([start_date, end_date, oblast])

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=['start_date', 'end_date', 'oblast'])

# Filter data for a specific oblast (e.g., 'Запорізька')
filtered_df = df[df['oblast'] == 'Запорізька'].copy()

# Convert date columns to datetime type
filtered_df['start_date'] = pd.to_datetime(filtered_df['start_date'])
filtered_df['end_date'] = pd.to_datetime(filtered_df['end_date'])

# Calculate duration in minutes and add it to the DataFrame, rounded to 1 decimal place
filtered_df['duration_minutes'] = ((filtered_df['end_date'] - filtered_df['start_date']).dt.total_seconds() / 60).round(1)

# Create a new column for the quarter
filtered_df['quarter'] = filtered_df['start_date'].dt.to_period('Q')

# Group by quarter and calculate the average duration in minutes
average_duration_per_quarter = filtered_df.groupby('quarter')['duration_minutes'].mean()

# Print the result
print(average_duration_per_quarter)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_alarms_data.csv', index=False)
