# -*- coding: utf-8 -*-
'''Eye Color Filter

    by Lawrence Huang and Christian Ominetti
    
                                            '''
        
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw
import numpy as np

def paste_item(x,y):
    #locates and imports the image
    #prompts decide which is base image and which is pasted
    filename = input("What is the name of the photo?")
    directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(directory, filename)
    img = plt.imread(filepath)
    #locates and imports a second image
    filename2 = input("What is the name of the image to paste on top?")
    directory2 = os.path.dirname(os.path.abspath(__file__))
    filepath2 = os.path.join(directory2, filename2)
    img2 = plt.imread(filepath2)
    #pastes 2nd image onto the first
    img.paste(img2,(x,y), mask = img2)
    #displays the image
    ax.imshow(img, interpolation = 'none')
    fig.show()