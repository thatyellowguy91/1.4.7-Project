import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw
import Image

directory = os.getcwd()
image = Image.open(student.jpg).show()

def blue_eye(x, y):
    for row in range(x[0], x[1]):
        for column in range(y[0], y[1]):
            if sum(img[row][column])>500:
                img[row][column]=[0, 0, 257]
