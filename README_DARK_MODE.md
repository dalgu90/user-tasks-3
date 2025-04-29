# Matplotlib Dark Mode Toggle Function

This repository contains an implementation of a `toggle_dark_mode` function for Matplotlib that allows users to easily switch their plots between dark mode and light mode themes.

## Features

The `toggle_dark_mode` function:

- Can be applied to either a specific axis, a figure, or the current figure if none is specified
- Converts the plot background to a dark color (#121212) when toggling to dark mode
- Inverts text colors from dark to light in dark mode
- Adjusts plot elements (grid lines, tick marks, etc.) to be visible on dark background
- Preserves the original colors of data elements (lines, points, bars) or provides an option to adjust them for better visibility
- Is fully reversible - calling the function again will toggle back to light mode
- Remembers the original state of all plot elements for proper restoration

## Implementation

The function has been implemented in two ways:

1. **Integrated with Matplotlib**: The function has been added to the `matplotlib.pyplot` module in the Matplotlib source code.
2. **Standalone Module**: A standalone version is provided in `matplotlib_dark_mode.py` that can be used with an existing Matplotlib installation.

## Usage

### Using the Standalone Module

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib_dark_mode import toggle_dark_mode

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
toggle_dark_mode(fig=fig)  # Apply dark mode to the figure
plt.show()

# Toggle back to light mode
toggle_dark_mode(fig=fig)  # Toggle back to light mode
plt.show()
```

After importing the module, you can also use the function directly through the pyplot interface:

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib_dark_mode  # This adds toggle_dark_mode to plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.toggle_dark_mode()  # Apply dark mode to current figure
plt.show()

# Toggle back to light mode
plt.toggle_dark_mode()  # Toggle back to light mode
plt.show()
```

### Using the Integrated Version

If you're using the modified Matplotlib source code:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.toggle_dark_mode()  # Apply dark mode to current figure
plt.show()

# Toggle back to light mode
plt.toggle_dark_mode()  # Toggle back to light mode
plt.show()
```

## Parameters

The `toggle_dark_mode` function accepts the following parameters:

- `ax` (optional): The axes to apply dark mode to. If None and fig is None, the current axes will be used.
- `fig` (optional): The figure to apply dark mode to. If None and ax is None, the current figure will be used.
- `preserve_data_colors` (default: True): If True, the original colors of data elements are preserved. If False, data colors will be adjusted for better visibility on dark background.

## Examples

The repository includes several example scripts:

1. `test_standalone_dark_mode.py`: Basic examples of using the function
2. `comprehensive_dark_mode_example.py`: More complex examples with various plot types
3. `dark_mode_toggle_demo.py`: Demonstrates toggling between dark and light modes
4. `test_plt_toggle.py`: Tests the toggle functionality using the plt interface

## Example Images

The repository includes several example images showing the function in action:

- `standalone_dark_mode_figure.png`: Dark mode applied to an entire figure
- `standalone_dark_mode_axis.png`: Dark mode applied to a specific axis
- `standalone_dark_mode_via_plt.png`: Dark mode applied using plt.toggle_dark_mode()
- `dark_vs_light_mode_comparison.png`: Comparison of dark mode and light mode
- `comprehensive_dark_mode_example.png`: Dark mode applied to various plot types
- `dark_mode_demo_dark.png` and `dark_mode_demo_light.png`: Comparison of the same plot in dark and light modes
- `integrated_dark_mode.png` and `integrated_light_mode.png`: Testing the integrated toggle functionality

## Installation

### Standalone Module (Recommended)

To use the standalone module, simply copy the `matplotlib_dark_mode.py` file to your project directory and import it as shown in the examples above.

### Integrated Version

To use the integrated version, you would need to install the modified Matplotlib source code:

1. Navigate to the `Phase 1/matplotlib-main` directory
2. Run `pip install -e .` to install the development version of Matplotlib with our modifications

**Note:** This is not recommended for production use as it modifies the core Matplotlib library. The standalone module provides the same functionality without modifying the core library.

### Alternative Approach

For a simpler approach that doesn't require modifying or reinstalling Matplotlib, you can use the standalone module but import it at the beginning of your script:

```python
import matplotlib.pyplot as plt
import matplotlib_dark_mode  # This adds toggle_dark_mode to plt
```

This will add the `toggle_dark_mode` function to the `plt` namespace, making it behave like the integrated version.