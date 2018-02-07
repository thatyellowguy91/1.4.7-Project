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
    img = plt.imread(filepath)
    fig, ax = plt.subplots(1, 1)
    height = len(img)
    width = len(img[0])
    for r in range(150,150):
        for c in range(150,150):
            img[r][c][157,157,157]
    #converts from numpy ndarry to PIL image
    img = PIL.Image.fromarray(img)
    #displays the image
    img.show()
    