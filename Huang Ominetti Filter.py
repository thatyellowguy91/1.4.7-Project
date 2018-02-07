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
    for r in range(604,1351):
        for c in range(883,1046):
            img[r][c][2]
    #displays the image
    ax.imshow(img, interpolation = 'none')
    fig.show()