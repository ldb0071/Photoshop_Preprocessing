import cv2 as cv2 
import numpy as np 
import matplotlib.pyplot as plt

############################################################################# Bluring Effect ####################################################################################################################################
#create a class that contains all bluring effects 

class bluring_effects:
    def __init__(self):
        pass
    
    #apply a box filter 
    def box_filter(self,image,size):
        #create a box filter 
        box_filter = np.ones((size,size),np.float32)/(size*size)
        #apply the filter to the image 
        image = cv2.filter2D(image,-1,box_filter)
        return image
    
    #apply a gaussian filter 
    def gaussian_blur(self,image,size):
        #create a gaussian filter 
        gaussian_filter = cv2.getGaussianKernel(size,0)
        #apply the filter to the image 
        image = cv2.filter2D(image,-1,gaussian_filter)
        return image
    
    #apply a median filter 
    def median_blur(self,image,size):
        #apply the filter to the image 
        image = cv2.medianBlur(image,size)
        return image
    
    #apply a bilateral filter 
    def bilateral_blur(self,image,size):
        #apply the filter to the image 
        image = cv2.bilateralFilter(image,size,75,75)
        return image
    
    #apply a motion blur 
    def motion_blur(self,image,size):
        #create a motion blur 
        motion_filter = np.zeros((size,size))
        motion_filter[int((size-1)/2),:] = np.ones(size)
        motion_filter = motion_filter/size
        #apply the filter to the image 
        image = cv2.filter2D(image,-1,motion_filter)
        return image
    
    #apply a zoom blur 
    def zoom_blur(self,image,size):
        #create a zoom blur 
        zoom_filter = np.zeros((size,size))
        zoom_filter[int((size-1)/2),int((size-1)/2)] = 1
        zoom_filter = cv2.GaussianBlur(zoom_filter,(size,size),0)
        #apply the filter to the image 
        image = cv2.filter2D(image,-1,zoom_filter)
        return image
    
    #apply a radial blur 
    def radial_blur(self,image,size):
        #create a radial blur 
        radial_filter = np.zeros((size,size))
        radial_filter[int((size-1)/2),int((size-1)/2)] = 1
        image = cv2.filter2D(image,-1,radial_filter)
        return image
    
    
############################################################################# MAIN ############################################################################################################################################   
#CREATE A  MAIN FUNCTION THAT CONTAINS THE APPLICATION OF THE BLURING EFFECTS AND THE  DISPLAY OF THE RESULTS USING MATPLOTLIB PLT  SUBPLOT
def main():
    #create an object of the class bluring_effects 
    bluring = bluring_effects()
    #read an image 
    image = cv2.imread("whats_heel.jpeg")
    #apply the box filter 
    box_filter = bluring.box_filter(image,3)
    #apply the gaussian filter 
    gaussian_blur = bluring.gaussian_blur(image,3)
    #apply the median filter 
    median_blur = bluring.median_blur(image,3)
    #apply the bilateral filter 
    bilateral_blur = bluring.bilateral_blur(image,3)
    #apply the motion blur 
    motion_blur = bluring.motion_blur(image,3)
    #apply the zoom blur 
    zoom_blur = bluring.zoom_blur(image,3)
    #apply the radial blur 
    radial_blur = bluring.radial_blur(image,3)
    #display the results 
    #create a figure 
    plt.figure(figsize=(10,10))
    #display the original image 
    plt.subplot(3,3,1)
    plt.imshow(image)
    plt.title("Original Image")
    #display the box filter 
    plt.subplot(3,3,2)
    plt.imshow(box_filter)
    plt.title("Box Filter")
    #display the gaussian blur 
    plt.subplot(3,3,3)
    plt.imshow(gaussian_blur)
    plt.title("Gaussian Blur")
    #display the median blur 
    plt.subplot(3,3,4)
    plt.imshow(median_blur)
    plt.title("Median Blur")
    #display the bilateral blur 
    plt.subplot(3,3,5)
    plt.imshow(bilateral_blur)
    plt.title("Bilateral Blur")
    #display the motion blur 
    plt.subplot(3,3,6)
    plt.imshow(motion_blur)
    plt.title("Motion Blur")
    #display the zoom blur 
    plt.subplot(3,3,7)
    plt.imshow(zoom_blur)
    plt.title("Zoom Blur")
    #display the radial blur 
    plt.subplot(3,3,8)
    plt.imshow(radial_blur)
    plt.title("Radial Blur")
    #show the figure 
    plt.show()
    
    
    
if __name__ == "__main__":
    main()