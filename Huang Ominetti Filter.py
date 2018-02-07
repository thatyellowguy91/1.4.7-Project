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
    filename = os.path.join(directory, 'student.jpg')
    if isPLT:
        img = PIL.Image.open(filename)
    else:
        img = PIL.Image.open(filepath)
    fig, axes = plt.subplots(1, 1)
    axes.imshow(img)
    for row in range(589, 1388):
        for column in range(883,1090):
            img[row][column]=[0, 0, 255]
    fig.show()

blue_eye()
