# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:49:16 2022

@author: Luiza
"""

from bioprinter import bioprint

bioprint(
    image_filename="dolly.jpeg",
    output_filename="dolly.csv",
    bg_color=[0, 0, 255],  # blue background represents empty wells
    pigments_wells={"A1": [0, 0, 0],        # black yeast in source well A1
                    "A2": [250, 120, 10],   # orange yeast in well A2
                    "A3": [255, 255, 255]}, # white yeast in well A3
    quantified_image_filename="dolly_preview.jpeg"
)