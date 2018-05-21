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

def paste_item(firstimg):
    directory = os.path.dirname(os.path.abspath(__file__))
    otherfile = os.path.join(directory, 'student.jpg') #selects the file
    img = PIL.Image.open(otherfile) #opens new image
    img.resize((30,30)) #resize new image
    firstimg.paste(img, (100,100)) #paste newimage at (100,100) on original image
    return firstimg