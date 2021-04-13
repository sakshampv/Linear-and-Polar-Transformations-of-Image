
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




def rotate(image, theta): #Rotating the image through center of image about the line perpendicular to the image plane by value theta in anti-clockwise direction
    m, n, o = image.shape #Image size x & y and RGB values
    image  = np.array(image) 
    center_y = m/2
    center_x = n/2
    
    x_mx = 2*int(round(center_x * math.cos(theta) + center_y * math.sin(theta) )) #New size of the rotated image
    y_mx = 2*int(round(center_y*math.cos(theta) + center_x * math.sin(theta)) ) #New size of the rotated image

    new_img = np.zeros((y_mx, x_mx, 3)) 

    for i in range(x_mx):
        for j in range(y_mx):
            x = ( i - x_mx/2) * math.cos(theta) - (j-y_mx/2) * math.sin(theta) + center_x #Translating the center of image as origin and then using the rotation matrix
            y = ( i - x_mx/2) * math.sin(theta) + (j-y_mx/2) * math.cos(theta) + center_y #Translating the center of image as origin and then using the rotation matrix
            x = int(round(x))
            y = int(round(y))
            if x >= 0 and x < n and y >= 0 and y < m:
                new_img[j][i] = image[y][x] #setting all the non negative values in the image
    new_img = new_img.astype(int) #converting the pixel values to integers
    return new_img
        
            

def flip(image): #Taking a mirror image about a plane passing through center and perpendicular to horizontal axis
    
    new_img = np.zeros(image.shape) 
    m, n, o = image.shape #Image size x & y and RGB values
    for i in range(m):
        for j in range(n):
             new_img[i][j] = image[i][n-j-1]
    new_img = new_img.astype(int)  #converting the pixel values to integers
    return new_img        
     


 
def translate(image, tx, ty):
    m, n, o = image.shape #Image size x & y and RGB values
    new_img = np.zeros((m + ty, n + tx, 3)) #increasing the image size by the translated amount
    for i in range(m):
        for j in range(n):
            new_img[i + ty][j + tx] = image[i][j] #using the translating transform
    new_img = new_img.astype(int) #converting the pixel values to integers
    return new_img         
            


def scale(image, factor):
    m, n, o = image.shape #Image size x & y and RGB values
    new_img = np.zeros((int(m/factor), int(n/factor), 3)) #Reducing the image size by factor

    for i in range( int(m/factor)):
        for j in range( int(n/factor)):
            new_img[i][j] = image[i*factor][j*factor] #Setting the pixel values of the new image
    new_img = new_img.astype(int) #converting the pixel values to integers
    return new_img         
                    
        
def shear(image, s):
    m, n, o = image.shape #Image size x & y and RGB values
    new_img = np.zeros((m,int(n + s*m), 3)) # Increasing the image size by the shear factor
    for i in range( int(n + s*m), ):
        for j in range(m): 
            x = i - s*j #Using the shear transform equations
            y = j
            x = int(x)
            y = int(y)
            if x >= 0 and x < n and y >= 0 and y < m:
                new_img[j][i] = image[y][x] #Setting the pixel values of the new image
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




#################################################################
     
# PART 2 A

new_img = rotate(image, math.pi/4)

scipy.misc.imsave('im2_rotate.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()
            
new_img = flip(new_img)
scipy.misc.imsave('im2_rotateflip.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()
            
# PART 2 B


new_img = translate(image,32, 32)

scipy.misc.imsave('im2_translate.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()

# PART 2 C

new_img = scale(image,3)

scipy.misc.imsave('im2_scale.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()
    
# PART 2 D

new_img = shear(image,0.2)
scipy.misc.imsave('im2_shear.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()

new_img = rotate(new_img, math.pi/2)
scipy.misc.imsave('im2_shear_rotate.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()

new_img = scale(new_img, 2)
scipy.misc.imsave('im2_shear_rotate_scale.jpg', new_img)  
imgplot = plt.imshow(new_img)
plt.show()

#################################################################


    
