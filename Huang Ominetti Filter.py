# -*- coding: utf-8 -*-
'''
    Eye Color Filter
    by Lawrence Huang and Christian Ominetti
    
                                            '''
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, 'student.jpg')
fig = PIL.Image.open(filepath)

def blue_eye(x, y):
    for row in range(x[0], x[1]):
        for column in range(y[0], y[1]):
            if sum(fig[row][column]):
                fig[row][column]=[0, 0, 255]
    fig.show()
