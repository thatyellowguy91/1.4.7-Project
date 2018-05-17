# -*- coding: utf-8 -*-
<<<<<<< HEAD
'''
    Eye Color Filter
    by Lawrence Huang and Christian Ominetti
    
                                            '''
=======
'''Eye Color Filter

    by Lawrence Huang and Christian Ominetti
    
                                            '''
        
>>>>>>> parent of 86e3d45... juss stuuffffs
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw
import numpy as np

<<<<<<< HEAD
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, 'student.jpg')
fig = PIL.Image.open(filepath)

<<<<<<< HEAD
def blue_eye(x, y):
    for row in range(x[0], x[1]):
        for column in range(y[0], y[1]):
<<<<<<< HEAD
            if sum(fig[row][column]):
                fig[row][column]=[0, 0, 255]
    fig.show()
=======
def background_change():
    #locates and imports the image
=======
def paste_item(x,y):
    #locates and imports the image
    #prompts decide which is base image and which is pasted
>>>>>>> parent of 86e3d45... juss stuuffffs
    filename = input("What is the name of the photo?")
    directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(directory, filename)
    img = plt.imread(filepath)
<<<<<<< HEAD
    fig, ax = plt.subplots(1, 1)
    height = len(img)
    width = len(img[0])
    for r in range(604,1351):
        for c in range(883,1046):
            img[r][c][2]
    #displays the image
    ax.imshow(img, interpolation = 'none')
    fig.show()
>>>>>>> parent of 6c0d574... Bob's big burgers
=======
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
>>>>>>> parent of 86e3d45... juss stuuffffs
=======
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 255]
    img.show()
>>>>>>> parent of 9336c4d... This Kinda Works!
