"""
Dark Mode Toggle Demo

This script demonstrates the toggle_dark_mode function that allows switching
between dark and light mode for matplotlib plots.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib_dark_mode import toggle_dark_mode

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Dark Mode Toggle Demo', fontsize=16)

# Plot 1: Line plot
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), 'r-', label='sin(x)')
axes[0, 0].plot(x, np.cos(x), 'b-', label='cos(x)')
axes[0, 0].set_title('Line Plot')
axes[0, 0].set_xlabel('X axis')
axes[0, 0].set_ylabel('Y axis')
axes[0, 0].grid(True)
axes[0, 0].legend()

# Plot 2: Scatter plot
n = 50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = (30 * np.random.rand(n))**2
axes[0, 1].scatter(x, y, s=area, c=colors, alpha=0.5)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('X axis')
axes[0, 1].set_ylabel('Y axis')
axes[0, 1].grid(True)

# Plot 3: Bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]
axes[1, 0].bar(categories, values, color='green')
axes[1, 0].set_title('Bar Plot')
axes[1, 0].set_xlabel('Categories')
axes[1, 0].set_ylabel('Values')
axes[1, 0].grid(True, axis='y')

# Plot 4: Histogram
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, alpha=0.7, color='purple')
axes[1, 1].set_title('Histogram')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].grid(True)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Create a function to toggle dark mode and save the figure
def toggle_and_save(state):
    if state:
        toggle_dark_mode(fig=fig)
        plt.savefig('dark_mode_demo_dark.png')
        print("Dark mode enabled - saved as dark_mode_demo_dark.png")
    else:
        toggle_dark_mode(fig=fig)
        plt.savefig('dark_mode_demo_light.png')
        print("Light mode enabled - saved as dark_mode_demo_light.png")

# Start in light mode
plt.savefig('dark_mode_demo_light.png')
print("Initial light mode - saved as dark_mode_demo_light.png")

# Toggle to dark mode
toggle_and_save(True)

# Toggle back to light mode
toggle_and_save(False)

# Toggle to dark mode again
toggle_and_save(True)

print("\nDemo completed. The toggle_dark_mode function successfully switches between dark and light modes.")