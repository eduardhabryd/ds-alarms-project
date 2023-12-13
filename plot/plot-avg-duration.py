import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from db.get_alarms import get_alarms

alarms = get_alarms()

data = []
for alarm in alarms:
    start_date = alarm.date
    end_date = alarm.alarmend.date
    oblast = alarm.oblast
    data.append([start_date, end_date, oblast])

df = pd.DataFrame(data, columns=['start_date', 'end_date', 'oblast'])

filtered_df = df[df['oblast'] == 'Кіровоградська'].copy()

filtered_df['start_date'] = pd.to_datetime(filtered_df['start_date'])
filtered_df['end_date'] = pd.to_datetime(filtered_df['end_date'])

filtered_df['duration_minutes'] = ((filtered_df['end_date'] - filtered_df['start_date']).dt.total_seconds() / 60).round(1)
filtered_df = filtered_df[filtered_df['duration_minutes'] < 900]

filtered_df['quarter'] = filtered_df['start_date'].dt.to_period('Q')

average_duration_per_quarter = filtered_df.groupby('quarter')['duration_minutes'].mean()

print(average_duration_per_quarter)

filtered_df.to_csv('filtered_alarms_data.csv', index=False)

plt.figure(figsize=(10, 6))
average_duration_per_quarter.plot(kind='line', marker='o', color='skyblue', linestyle="-")
plt.title('Average Duration of Alarms in Kirovogradska region per Quarter')
plt.xlabel('Quarter')
plt.ylabel('Average Duration (minutes)')
plt.savefig('alarms_avg_duration.png')
