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
    },
}    

class FigureStyleManager:
