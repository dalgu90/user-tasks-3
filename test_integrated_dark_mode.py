"""
Test script for the integrated toggle_dark_mode function in matplotlib.pyplot.

This script creates a simple plot and applies dark mode to it using the
toggle_dark_mode function that has been integrated into matplotlib.pyplot.
"""

import sys
import os

# Add the matplotlib-main directory to the Python path
sys.path.insert(0, os.path.abspath('Phase 1/matplotlib-main'))

import numpy as np
import matplotlib.pyplot as plt

# Create a simple plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot data in both subplots
ax1.plot(x, y1, 'r-', label='sin(x)')
ax1.set_title('Dark Mode')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.grid(True)
ax1.legend()

ax2.plot(x, y2, 'b-', label='cos(x)')
ax2.set_title('Default Mode')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.grid(True)
ax2.legend()

# Apply dark mode to the first subplot only
plt.toggle_dark_mode(ax=ax1)

# Add a main title
fig.suptitle('Testing Integrated Dark Mode Function', fontsize=16)

# Save the figure
plt.savefig('integrated_dark_mode_test.png')
print("Test image saved as integrated_dark_mode_test.png")

# Show the plot (uncomment if running interactively)
# plt.show()