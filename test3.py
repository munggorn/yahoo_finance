from test1 import last_100_weeks_z_scores
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')
exec(open('C:/Users/User/.venv/test2.py').read())
exec(open('C:/Users/User/.venv/test1.py').read())
# Plotting the filtered data
fig, ax = plt.subplots(figsize=(10, 6))
last_100_weeks_z_scores.plot(ax=ax, grid=True, linestyle='-', marker='o')

plt.xlabel('Weeks')
plt.ylabel('Z-Scores')
plt.title('Z-Scores')
plt.legend(loc='upper left')
ax.axhline(0, color='red', linestyle='--', linewidth=2)
plt.show()
