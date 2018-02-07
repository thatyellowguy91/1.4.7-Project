# -*- coding: utf-8 -*-
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


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def colorific(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with radius = 30% of short side
        new_image = eye_change
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
