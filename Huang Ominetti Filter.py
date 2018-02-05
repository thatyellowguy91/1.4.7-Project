import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            
import student.jpg
directory = os.getcwd()
filepath = os.path.join(directory)

def blue_eye(x, y):
    for row in range(x[0], x[1]):
        for column in range(y[0], y[1]):
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 257]
                

                
