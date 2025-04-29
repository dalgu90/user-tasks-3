"""
Comprehensive example of the toggle_dark_mode function.

This script demonstrates the toggle_dark_mode function with various plot types
and configurations.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib_dark_mode import toggle_dark_mode

# Create a figure with multiple subplots and different plot types
fig = plt.figure(figsize=(12, 10))

# Line plot
ax1 = fig.add_subplot(2, 2, 1)
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'r-', label='sin(x)')
ax1.plot(x, np.cos(x), 'b-', label='cos(x)')
ax1.set_title('Line Plot')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.grid(True)
ax1.legend()

# Scatter plot
ax2 = fig.add_subplot(2, 2, 2)
n = 50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = (30 * np.random.rand(n))**2
ax2.scatter(x, y, s=area, c=colors, alpha=0.5)
ax2.set_title('Scatter Plot')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.grid(True)

# Bar plot
ax3 = fig.add_subplot(2, 2, 3)
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]
ax3.bar(categories, values, color='green')
ax3.set_title('Bar Plot')
ax3.set_xlabel('Categories')
ax3.set_ylabel('Values')
ax3.grid(True, axis='y')

# Histogram
ax4 = fig.add_subplot(2, 2, 4)
data = np.random.randn(1000)
ax4.hist(data, bins=30, alpha=0.7, color='purple')
ax4.set_title('Histogram')
ax4.set_xlabel('Value')
ax4.set_ylabel('Frequency')
ax4.grid(True)

# Add a main title
fig.suptitle('Dark Mode Example with Various Plot Types', fontsize=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Apply dark mode to the entire figure
toggle_dark_mode(fig=fig)

# Save the figure
plt.savefig('comprehensive_dark_mode_example.png')

# Create a split example (half dark mode, half normal)
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Create identical plots in both axes
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

for ax in [ax1, ax2]:
    ax.plot(x, y1, 'r-', label='sin(x)')
    ax.plot(x, y2, 'b-', label='cos(x)')
    ax.set_title('Sine and Cosine')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.grid(True)
    ax.legend()

# Apply dark mode only to the left axis
toggle_dark_mode(ax=ax1)

# Add a main title
fig2.suptitle('Dark Mode vs. Light Mode Comparison', fontsize=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the figure
plt.savefig('dark_vs_light_mode_comparison.png')

print("Examples saved as comprehensive_dark_mode_example.png and dark_vs_light_mode_comparison.png")