import matplotlib.pyplot as plt
import numpy as np

# Data for Registers (ordered alphabetically)
benchmarks = ['Memory', 'Register']
benign = [99.8, 96.9]
sdc = [0, 0]
crash = [0.2, 3.1]

# Convert data to numpy arrays for easier manipulation
benign = np.array(benign)
sdc = np.array(sdc)
crash = np.array(crash)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 4))

# Plot stacked bars
ax.bar(benchmarks, benign, label='Benign', color='green', width=0.5)
ax.bar(benchmarks, sdc, bottom=benign, label='SDC', color='orange', width=0.5)
ax.bar(benchmarks, crash, bottom=benign + sdc, label='Crash', color='red', width=0.5)

# Add labels and title
ax.set_ylabel('Percentage')
ax.set_yscale('exp')
ax.set_title('OS Injection Campaign results')

# Set y-axis limits to match the exact height of the highest bars
ax.set_ylim(1, max(benign + sdc + crash))

# Move the legend to the right side
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout to make room for the legend
plt.tight_layout()

plt.savefig('os.png')
# Display the plot
plt.show()
