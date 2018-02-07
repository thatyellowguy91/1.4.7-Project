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
    top_left_cordinates = input("Please enter the first set of coordinates for the eye locations.")
    bottom_right_coordinates = input("Please enter the second set of coordinates for the eye location.")
    for row in range(top_left_coordinates[0], bottom_right_coordinates[0]):
        for column in range(top_left_coordinates[1], bottom_right_coordinates[1]):
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 255]

print("Please enter coordinates in list form when prompted.  Enter 'eye_change()' to begin.")