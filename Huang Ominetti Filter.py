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

def no_color(orig):
    i = orig #sets the variable for the selected image
    directory = os.path.dirname(os.path.abspath(__file__)) #selects path of directory
    File = os.path.join(directory, i) #selects a specific file as the directory
    img = plt.imread(File) #enables the file to be opened as a plt
    fig, ax = plt.subplots(1, 1) #creates subplots
    height = len(img) #matches the height to the y value of the image 
    width = len(img[0]) #matches the width to the x value of the image
    for r in range(height): 	#sets up the nested loop
        for c in range(width):
            if sum(img[r][c])<100: #scans RGB values to determine if the sum is less than or greater than 100 within a given area
                img[r][c] = [0,0,255]
            img[r][c]=[sum(img[r][c])/3] #divides the sum of the RGB values in the givin area by 3
    ax.set_axis_off() #hides the axes			
    ax.imshow(img, interpolation='none')
    fig.savefig('temp.jpg') #saves the file as a .jpg file
    result = os.path.join(directory, 'temp.jpg') #sets the new file as result
    img = PIL.Image.open(result) #uses PIL to open the image
    img.show() #enables the file to be saved in folder
