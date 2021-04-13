
import numpy as np #for matrix operations
import matplotlib.image as img #for plotting the image pixels as images
import math 
import scipy.misc #for saving image in JPG format
from matplotlib import pyplot as plt

def polar_transform(image):
    m, n, o = image.shape #Image size x & y and RGB values
    center_y = m/2
    center_x = n/2
    r = math.sqrt( center_x * center_x + center_y * center_y )
    r = int(r) #The radius size of the image
    new_img = np.zeros((r,300, 3)) #Size of the image as (radius, no. of different angles, RGB)
    for i in range(r):
        for j in range(300):
            theta = j * math.pi / 150 
            x = center_x + i*math.cos(theta)
            y= center_y + i * math.sin(theta)
            x = int(x)
            y = int(y)

            if x >= 0 and x < n and y >= 0 and y < m:
 
               new_img[i][j] = image[y][x] #setting all the non negative values in the image
    new_img = new_img.astype(int) #converting the pixel values to integers        
    return new_img





#################################################################   

# Image Import
image = img.imread("im2.jpg")
image  = np.array(image)

#################################################################   

#################################################################            
          
# PART 1

new_img = polar_transform(image)
scipy.misc.imsave('im2_polar.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()
  
#################################################################

