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

def eye_change(x, y):
    color = input('What color would you like your eye?')
    if color == "Blue" or "blue":
        for row in range(x[0], x[1]):
            for column in range(y[0], y[1]):
                if sum(img[row][column])>500:
                    img[row][column]=[0, 0, 255]
