'''Eye Color Filter

    by Lawrence Huang and Christian Ominetti
    
    '''
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

directory = os.getcwd()
image_list = []
file_list = []

def blue_eye():
    tlc = int(input("Please enter the first set of coordinates for the eye locations."))
    brc = int(input("Please enter the second set of coordinates for the eye location."))
    for row in range(tlc[0], brc[0]):
        for column in range(tlc[1], brc[1]):
                img[row][column]=[0, 0, 255]

print("Please enter coordinates in list form when prompted.  Enter 'blue_eye()' to begin.")