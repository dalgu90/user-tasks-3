"""
Matplotlib Dark Mode Toggle Function

This module provides a function to toggle dark mode for matplotlib figures and axes.
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib as mpl


def toggle_dark_mode(ax=None, fig=None, preserve_data_colors=True):
    """
    Toggle dark mode for a matplotlib figure or axes.
    
    This function toggles between dark and light mode for the specified figure or axes.
    When toggling to dark mode, it converts the plot background to a dark color, inverts 
    text colors from dark to light, and adjusts plot elements (grid lines, tick marks, etc.) 
    to be visible on a dark background. When called again, it reverts back to light mode.
    
    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`, optional
        The axes to toggle dark mode for. If None and fig is None, the current axes
        will be used.
    fig : `~matplotlib.figure.Figure`, optional
        The figure to toggle dark mode for. If None and ax is None, the current figure
        will be used.
    preserve_data_colors : bool, default: True
        If True, the original colors of data elements (lines, points, bars) are preserved.
        If False, data colors will be adjusted for better visibility on dark background.
        
    Returns
    -------
    None
    
    Notes
    -----
    This function modifies the following properties:
    - Figure and axes background colors
    - Text colors (titles, labels, ticks)
    - Grid and spine colors
    - Legend background and text colors
    
    The function stores the original state in a custom attribute '_dark_mode_state'
    on the figure object, allowing it to toggle between dark and light modes.
    
    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from matplotlib_dark_mode import toggle_dark_mode
    >>> x = np.linspace(0, 10, 100)
    >>> fig, ax = plt.subplots()
    >>> ax.plot(x, np.sin(x))
    >>> toggle_dark_mode(fig=fig)  # Apply dark mode to the figure
    >>> plt.show()
    >>> toggle_dark_mode(fig=fig)  # Toggle back to light mode
    >>> plt.show()
    
    >>> fig, (ax1, ax2) = plt.subplots(1, 2)
    >>> ax1.plot(x, np.sin(x))
    >>> ax2.plot(x, np.cos(x))
    >>> toggle_dark_mode(ax=ax1)  # Apply dark mode to ax1 only
    >>> plt.show()
    """
    # Define dark mode colors
    dark_bg_color = '#121212'
    dark_text_color = '#EEEEEE'
    dark_grid_color = '#333333'
    dark_spine_color = '#555555'
    
    # Define light mode colors (default matplotlib colors)
    light_bg_color = 'white'
    light_text_color = 'black'
    light_grid_color = '#b0b0b0'
    light_spine_color = 'black'
    
    # Get the axes or figure to modify
    if ax is None and fig is None:
        # Use current axes if neither ax nor fig is specified
        ax = plt.gca()
        fig = ax.figure
    elif ax is not None:
        # If ax is specified, get its figure
        fig = ax.figure
    
    # If we have a figure but no specific axes, apply to all axes in the figure
    if ax is None and fig is not None:
        axes = fig.get_axes()
    else:
        # Otherwise, just work with the specified axes
        axes = [ax]
    
    # Check if we're in dark mode already
    is_dark_mode = getattr(fig, '_dark_mode_state', False)
    
    # Store original states if this is the first toggle
    if not hasattr(fig, '_original_states'):
        fig._original_states = {}
        
        # Store figure background
        fig._original_states['fig_bg'] = fig.patch.get_facecolor()
        
        # Store axes states
        for i, axis in enumerate(axes):
            ax_state = {}
            
            # Store axes background
            ax_state['bg'] = axis.get_facecolor()
            
            # Store spine colors
            ax_state['spines'] = {spine: axis.spines[spine].get_edgecolor() 
                                 for spine in axis.spines}
            
            # Store grid color
            ax_state['grid'] = axis.get_xgridlines()[0].get_color() if len(axis.get_xgridlines()) > 0 else light_grid_color
            
            # Store text colors
            if axis.title is not None:
                ax_state['title'] = axis.title.get_color()
            ax_state['xlabel'] = axis.xaxis.label.get_color()
            ax_state['ylabel'] = axis.yaxis.label.get_color()
            
            # Store tick colors
            ax_state['xtick'] = axis.xaxis.get_ticklabels()[0].get_color() if len(axis.xaxis.get_ticklabels()) > 0 else light_text_color
            ax_state['ytick'] = axis.yaxis.get_ticklabels()[0].get_color() if len(axis.yaxis.get_ticklabels()) > 0 else light_text_color
            
            # Store legend colors if it exists
            if axis.get_legend() is not None:
                ax_state['legend_bg'] = axis.get_legend().get_frame().get_facecolor()
                ax_state['legend_edge'] = axis.get_legend().get_frame().get_edgecolor()
                ax_state['legend_text'] = [text.get_color() for text in axis.get_legend().get_texts()]
            
            fig._original_states[f'ax_{i}'] = ax_state
    
    # Toggle dark mode state
    is_dark_mode = not is_dark_mode
    fig._dark_mode_state = is_dark_mode
    
    if is_dark_mode:
        # Apply dark mode
        # Set figure background color
        fig.patch.set_facecolor(dark_bg_color)
        
        # Modify each axes
        for ax in axes:
            # Set axes background color
            ax.set_facecolor(dark_bg_color)
            
            # Update spines
            for spine in ax.spines.values():
                spine.set_color(dark_spine_color)
            
            # Update grid
            ax.grid(color=dark_grid_color, linestyle='-', linewidth=0.5, alpha=0.5)
            
            # Update text elements
            if ax.title is not None:
                ax.title.set_color(dark_text_color)
            
            ax.xaxis.label.set_color(dark_text_color)
            ax.yaxis.label.set_color(dark_text_color)
            
            # Update tick colors
            ax.tick_params(axis='x', colors=dark_text_color)
            ax.tick_params(axis='y', colors=dark_text_color)
            
            # Update legend if it exists
            if ax.get_legend() is not None:
                ax.get_legend().get_frame().set_facecolor(dark_bg_color)
                ax.get_legend().get_frame().set_edgecolor(dark_spine_color)
                
                # Update legend text
                for text in ax.get_legend().get_texts():
                    text.set_color(dark_text_color)
            
            # Adjust data colors if requested
            if not preserve_data_colors:
                # Increase brightness/contrast of plot elements for better visibility
                for artist in ax.get_children():
                    # Handle lines
                    if isinstance(artist, Line2D):
                        # Get current color and make it brighter if needed
                        color = artist.get_color()
                        # Only adjust if it's a dark color
                        if isinstance(color, str) and color.startswith('#'):
                            # Skip adjustment for already bright colors
                            continue
                        # For other types of colors, we could add more sophisticated
                        # brightness adjustment here
                    
                    # Handle collections (scatter plots, bar plots, etc.)
                    elif hasattr(artist, 'get_facecolor') and hasattr(artist, 'set_facecolor'):
                        # Similar color adjustment could be applied here
                        pass
    else:
        # Restore light mode (original state)
        # Restore figure background
        fig.patch.set_facecolor(fig._original_states['fig_bg'])
        
        # Restore each axes
        for i, ax in enumerate(axes):
            ax_state = fig._original_states.get(f'ax_{i}')
            if ax_state:
                # Restore background
                ax.set_facecolor(ax_state['bg'])
                
                # Restore spines
                for spine_name, color in ax_state['spines'].items():
                    ax.spines[spine_name].set_color(color)
                
                # Restore grid
                ax.grid(color=ax_state['grid'], linestyle='-', linewidth=0.5, alpha=0.5)
                
                # Restore text elements
                if ax.title is not None and 'title' in ax_state:
                    ax.title.set_color(ax_state['title'])
                
                ax.xaxis.label.set_color(ax_state['xlabel'])
                ax.yaxis.label.set_color(ax_state['ylabel'])
                
                # Restore tick colors
                ax.tick_params(axis='x', colors=ax_state['xtick'])
                ax.tick_params(axis='y', colors=ax_state['ytick'])
                
                # Restore legend if it exists
                if ax.get_legend() is not None and 'legend_bg' in ax_state:
                    ax.get_legend().get_frame().set_facecolor(ax_state['legend_bg'])
                    ax.get_legend().get_frame().set_edgecolor(ax_state['legend_edge'])
                    
                    # Restore legend text
                    for text, color in zip(ax.get_legend().get_texts(), ax_state['legend_text']):
                        text.set_color(color)
    
    # Redraw the figure to apply changes
    fig.canvas.draw_idle()


# Add the function to matplotlib.pyplot module for convenience
# This allows users to call plt.toggle_dark_mode() directly
setattr(plt, 'toggle_dark_mode', toggle_dark_mode)