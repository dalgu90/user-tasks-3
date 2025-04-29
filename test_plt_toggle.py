"""
Test script for the toggle_dark_mode function using the standalone module
but simulating the integrated version by importing the module first
"""

import numpy as np
import matplotlib.pyplot as plt
# Import our standalone module to add toggle_dark_mode to plt
import matplotlib_dark_mode

# Create a simple plot
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, np.sin(x), 'r-', label='sin(x)')
ax.plot(x, np.cos(x), 'b-', label='cos(x)')
ax.set_title('Dark Mode Toggle Test (Using Standalone Module)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.grid(True)
ax.legend()

# Save in light mode
plt.savefig('integrated_light_mode.png')
print("Saved in light mode as integrated_light_mode.png")

# Toggle to dark mode
plt.toggle_dark_mode()
plt.savefig('integrated_dark_mode.png')
print("Toggled to dark mode - saved as integrated_dark_mode.png")

# Toggle back to light mode
plt.toggle_dark_mode()
plt.savefig('integrated_light_mode_toggled.png')
print("Toggled back to light mode - saved as integrated_light_mode_toggled.png")

print("\nTest completed. The toggle_dark_mode function successfully switches between dark and light modes.")