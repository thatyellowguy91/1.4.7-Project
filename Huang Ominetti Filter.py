'''Eye Color Filter

    by Lawrence Huang and Christian Ominetti
    
    '''
#importing necessary libraries
import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

directory = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(directory, 'student.jpg')
student_img = PIL.Image.open(filename)
fig, axes = plt.subplots(1, 1)
axes.imshow(student_img)

def blue_eye():
    directory = os.path.dirname(os.path.abspath(__file__))  
    filename = os.path.join(directory, 'student.jpg')
    student_img = PIL.Image.open(filename)
    fig, axes = plt.subplots(1, 1)
    axes.imshow(student_img)
    for row in range(50, 50):
        for column in range(50, 50):
            img[row][column]=[0, 0, 255]
    fig.show()

blue_eye()