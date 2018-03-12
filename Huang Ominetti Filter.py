# -*- coding: utf-8 -*-
'''Eye Color Filter
    by Lawrence Huang and Christian Ominetti
    
                                            '''
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

directory = os.getcwd()
img = open('student.jpg')

def blue_eye(x, y):
    for row in range(x[0], x[1]):
        for column in range(y[0], y[1]):
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 255]
    fig, ax = plt.subplots(1, 1)
    fig.show()