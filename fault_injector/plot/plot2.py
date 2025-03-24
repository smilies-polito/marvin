import matplotlib.pyplot as plt
import numpy as np

# Data for Registers (ordered alphabetically)
benchmarks = ['Basicmath', 'Dijkstra', 'Qsort', 'Rijndeal', 'SHA', 'Stringsearch']
benign_registers = [94.3, 95, 96.2, 69.4, 88.4, 99.5]
sdc_registers = [5.3, 4.4, 2.6, 29.6, 11.2, 0.3]
crash_registers = [0.4, 0.6, 1.2, 1, 0.4, 0.2]

# Data for Memory (ordered alphabetically)
benign_memory = [99.7, 96.9, 98.5, 98.7, 95, 99.9]
sdc_memory = [0.1, 0.7, 0.9, 0.8, 3.9, 0.0]
crash_memory = [0.2, 2.4, 0.6, 0.5, 1.1, 0.1]

# Create a figure with two subplots (one over the other)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# X positions for the bars (one for each benchmark)
x_registers = np.arange(len(benchmarks))
x_memory = np.arange(len(benchmarks))

# Set bar width
bar_width = 0.6  # Reduced width for the bars

# Plot stacked bars for Registers (Top Plot)
ax1.bar(x_registers, benign_registers, label='Benign', color='green', width=bar_width)
ax1.bar(x_registers, sdc_registers, bottom=benign_registers, label='SDC', color='orange', width=bar_width)
ax1.bar(x_registers, crash_registers, bottom=np.array(benign_registers) + np.array(sdc_registers), label='Crash', color='red', width=bar_width)
ax1.set_xlabel('Benchmarks')
ax1.set_ylabel('Percentage (%)')
ax1.set_title('Registers Injection Results', fontweight='bold')  # Bold title
ax1.set_xticks(x_registers)
ax1.set_xticklabels(benchmarks)
ax1.set_ylim([0, 100])

# Plot stacked bars for Memory (Bottom Plot)
ax2.bar(x_memory, benign_memory, label='Benign', color='green', width=bar_width)
ax2.bar(x_memory, sdc_memory, bottom=benign_memory, label='SDC', color='orange', width=bar_width)
ax2.bar(x_memory, crash_memory, bottom=np.array(benign_memory) + np.array(sdc_memory), label='Crash', color='red', width=bar_width)
ax2.set_xlabel('Benchmarks')
ax2.set_ylabel('Percentage (%)')
ax2.set_title('Memory Injection Results', fontweight='bold')  # Bold title
ax2.set_xticks(x_memory)
ax2.set_xticklabels(benchmarks)
ax2.set_ylim([0, 100])

# Add a single legend on the side
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Make room for the legend on the right

# Save the plot as an image file
plt.savefig('registers_memory_injection_results_vertical_bold_title.png')

# Show the plot
plt.show()
