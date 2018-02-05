import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            
import student.jpg

directory = os.getcwd()
filepath = os.path.join(directory)

def blue_eye(x, y):
    for row in range(x[749.304], x[1206.07]):
        for column in range(y[976.332], y[1009.26]):
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 257]
                

                
