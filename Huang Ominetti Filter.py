# -*- coding: utf-8 -*-
'''Eye Color Filter
    by Lawrence Huang and Christian Ominetti
    
                                                '''
        
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

#imports the image
def blue_eye():
    directory = os.path.dirname(os.path.abspath(__file__))  
    img = PIL.Image.open(directory, 'student.jpg')
    axes.imshow(img)
    for r in range(589, 1388):
        for c in range(883,1090):
            img[r][c][2]=img[r][c][1]
    fig.show()

def background_change():
    filename = input("What is the name of the photo?")
    directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(directory, filename)
    img = PIL.Image.open(filepath)
    img.show()
    