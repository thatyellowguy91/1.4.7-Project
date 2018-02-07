# -*- coding: utf-8 -*-
'''Eye Color Filter
    by Lawrence Huang and Christian Ominetti
    
                                                '''
        
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

def background_change():
    #locates and imports the image
    filename = input("What is the name of the photo?")
    directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(directory, filename)
    img = PIL.Image.open(filepath)
    #displays the image
    img.show()
    