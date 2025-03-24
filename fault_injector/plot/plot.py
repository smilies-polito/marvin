import matplotlib.pyplot as plt
import numpy as np

# Data
campaigns = ['Basicmath-single', 'Basicmath-multi', 'Dijkstra-single', 'Dijkstra-multi', 
             'Quicksort-single', 'Quicksort-multi', 'Rijndeal-single', 'Rijndeal-multi', 
             'SHA-single', 'SHA-multi', 'Stringsearch-single', 'Stringsearch-multi']
benign = [94.3, 43.8, 95, 97.1, 96.2, 77.7, 69.4, 7, 88.4, 43.8, 99.5, 95.7]  # Percentage of benign
sdc = [5.3, 11.8, 4.4, 2.6, 2.6, 21.6, 29.6, 38.3, 11.2, 55.4, 0.3, 4.1]     # Percentage of SDC (Silent Data Corruption)
crash = [0.4, 44.4, 0.6, 0.3, 1.2, 0.7, 1, 54.7, 0.4, 1.8, 0.2, 0.2]   # Percentage of Crash/Hang

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# X positions for the bars with space between different benchmarks
x = np.array([0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16])

# Plotting the stacked bars
ax.bar(x, benign, label='Benign', color='green')
ax.bar(x, sdc, bottom=benign, label='SDC', color='orange')
ax.bar(x, crash, bottom=np.array(benign) + np.array(sdc), label='Crash/Hang', color='red')

# Adding labels and title
ax.set_ylabel('Percentage (%)')
ax.set_ylim([0, 100])

# Custom x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(['SBU', 'MBU'] * 6)

# Adding benchmark names under the groups
for i, label in enumerate(['Basicmath', 'Dijkstra', 'Quicksort', 'Rijndeal', 'SHA', 'Stringsearch']):
    ax.text((x[2*i] + x[2*i+1]) / 2, -10, label, ha='center', va='top', fontsize=12, fontweight='bold')

# Moving the legend outside to the right
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust the layout to ensure everything fits
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Save the plot as an image file
image_path = 'stacked_bar_multibit_expanded.png'
plt.savefig(image_path)

# Show the plot
plt.show()
