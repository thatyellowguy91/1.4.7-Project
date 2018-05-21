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

def colour(orig):
    i = orig #set variable for image
    directory = os.path.dirname(os.path.abspath(__file__)) #set path of directory
    File = os.path.join(directory, i) #set the directory to a specific file
    img = plt.imread(File) #allow the file to be opened in plt
    fig, ax = plt.subplots(1, 1) #create subplots
    height = len(img) #set height variable to y values of image
    width = len(img[0]) #set width variable x values of image
    for r in range(height): 	#set up nested loop
        for c in range(width):
            if sum(img[r][c])<100: #test for if sum of RGB values in selected area is less than 100
                img[r][c] = [2,255,255]
            img[r][c]=[sum(img[r][c])/3] #takes the sum of the RGB values in the selected area, divided by three
    ax.set_axis_off() #hides the axes			
    ax.imshow(img, interpolation='none')
    fig.savefig('temp.jpg') #save as .jpg file
    result = os.path.join(directory, 'temp.jpg') #sets the new file as result
    img = PIL.Image.open(result) #opens the image using PIL
    img.show() #allows file to be saved into folder
