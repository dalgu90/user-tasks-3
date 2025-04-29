"""
Test script for the standalone toggle_dark_mode function.

This script creates various plots and applies dark mode to them using the
toggle_dark_mode function from the matplotlib_dark_mode module.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib_dark_mode import toggle_dark_mode

# Test 1: Apply dark mode to entire figure
print("Test 1: Dark mode applied to entire figure")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(x, y1, 'r-', label='sin(x)')
ax1.plot(x, y2, 'b-', label='cos(x)')
ax1.set_title('Dark Mode Applied to Figure')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.grid(True)
ax1.legend()
toggle_dark_mode(fig=fig1)
fig1.savefig('standalone_dark_mode_figure.png')

# Test 2: Apply dark mode to specific axis
print("Test 2: Dark mode applied to specific axis")
fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(10, 4))
ax2a.plot(x, y1, 'r-', label='sin(x)')
ax2a.set_title('Dark Mode Applied')
ax2a.set_xlabel('X axis')
ax2a.set_ylabel('Y axis')
ax2a.grid(True)
ax2a.legend()

ax2b.plot(x, y2, 'b-', label='cos(x)')
ax2b.set_title('Default Mode')
ax2b.set_xlabel('X axis')
ax2b.set_ylabel('Y axis')
ax2b.grid(True)
ax2b.legend()

toggle_dark_mode(ax=ax2a)
fig2.savefig('standalone_dark_mode_axis.png')

# Test 3: Apply dark mode with color adjustment
print("Test 3: Dark mode with color adjustment")
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(x, y1, 'r-', label='sin(x)')
ax3.plot(x, y2, 'b-', label='cos(x)')
ax3.set_title('Dark Mode with Color Adjustment')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.grid(True)
ax3.legend()
toggle_dark_mode(fig=fig3, preserve_data_colors=False)
fig3.savefig('standalone_dark_mode_color_adjusted.png')

# Test 4: Using the function through plt
print("Test 4: Using plt.toggle_dark_mode()")
fig4, ax4 = plt.subplots(figsize=(8, 4))
ax4.plot(x, y1, 'r-', label='sin(x)')
ax4.plot(x, y2, 'b-', label='cos(x)')
ax4.set_title('Dark Mode via plt.toggle_dark_mode()')
ax4.set_xlabel('X axis')
ax4.set_ylabel('Y axis')
ax4.grid(True)
ax4.legend()
plt.toggle_dark_mode(fig=fig4)
fig4.savefig('standalone_dark_mode_via_plt.png')

print("Test images saved as standalone_dark_mode_*.png")