import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import smooth_transition

# Create initial and final data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Line plot transition
fig1, ax1 = plt.subplots()
line, = ax1.plot(x, y1, label='Line Transition')
ani1 = smooth_transition(y1, y2, duration=2.0, fps=30, fig=fig1, ax=ax1)

# Scatter plot transition
fig2, ax2 = plt.subplots()
scatter = ax2.scatter(x, y1, label='Scatter Transition')
ani2 = smooth_transition(y1, y2, duration=2.0, fps=30, fig=fig2, ax=ax2, x=x)

# Bar plot transition
fig3, ax3 = plt.subplots()
bars = ax3.bar(x, y1, label='Bar Transition')

# Pass the `bars` object to the `smooth_transition` function
ani3 = smooth_transition(y1, y2, duration=2.0, fps=30, fig=fig3, ax=ax3, bars=bars.patches)

# Save animations as MP4 files
ani1.save('line_transition.mp4', writer='ffmpeg')
ani2.save('scatter_transition.mp4', writer='ffmpeg')
ani3.save('bar_transition.mp4', writer='ffmpeg')

# Display all animations
plt.show()