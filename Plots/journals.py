### Author: OptimusThi

"""
Publication-Quality Figure Style Manager
Easily create figures conforming to different journal and presentation requirements
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
import json

# ==============================================================
# STYLE CONFIGURATIONS FOR DIFFERENT JOURNALS AND FORMATS
# ==============================================================

# Unfinished!
STYLE_CONFIGS = {
    'Physical_Review_C': {        
        'description': 'Physical Review C (APS) style', 
        'figure_width_single': 3.4 # inches (single column)
        'figure_width_double': 7.0, # inches (double column)
        'figure_height_max': 9.0, # inches
        'dpi': 600, # resolution
        'font_family': 'serif',
        'font_serif': ['Times', 'Times New Roman'],
        'font_size': 8, # base font size
        'axes_labelsize': 9, 
        'axes_titlesize': 9, 
        'xtick_labelsize': 8,
        'ytick_labelsize': 8,
        'legend_fontsize': 8,
        'line_width': 1.0,
        'marker_size': 4,
        'axes_linewidth': 0.8,
        'grid': False,
        'legend_frameon': False, 
        'file_format': ['pdf', 'eps'],
        'tight_layout': True,
    },
}    

class FigureStyleManager:
    """
    Manager class for creating publication-quality figures
    """
    
    def __init__(self, style='Physical_Review_C', column='single'):
    """
    Initialize the style manager
    
    Parameters:
    -----------
    style : str
        Name of the style configuration (e.g., 'Physical_Review_C')
    column : str 
        'single' or 'double' column width
    """
    if style not in STYLE_CONFIGS:
        available = ', '.join(STYLE_CONFIGS.keys()) 
        raise ValueError(f"Style '{style}' not found. Available: {available}")
    
    self.style_name = style
    self.config = STYLE_CONFIGS[style].copy()
    self.column = column
    self._apply_style()           
    
    ### Next step: _apply_style function     
