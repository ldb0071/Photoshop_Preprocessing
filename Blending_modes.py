#Importing libraries
import cv2 as cv2
import numpy as np 
import matplotlib.pyplot as plt




                ################################ BLENDING MODES #################################
                
class blending_mode():
    
    def __init__(self):
        pass
    
    # Image multiply mode
    def multiply(self,image_1,image_2):
    
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1*image_2
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def lighten(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.maximum(image_1,image_2)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def diffusion(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-(2*image_1*image_2)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def overlay(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def soft_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def hard_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def color_dodge(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1/(1-image_2)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def linear_burn(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-1
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def color_burn(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=1-(1-image_1)/(image_2)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def linear_dodge(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2
        image_3=image_3*255
        return image_3
    
  
    # Image multiply mode
    def linear_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-1
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def vivid_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where(image_2<0.5,1-(1-image_1)/(2*image_2),image_1/(2*(1-image_2)))
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def pin_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where(image_2<0.5,np.minimum(image_1,2*image_2),np.maximum(image_1,2*(image_2-0.5)))
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def hard_mix(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where((image_1+image_2)<1,0,1)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def difference(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.abs(image_1-image_2)
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def exclusion(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-2*image_1*image_2
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def subtract(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1-image_2
        image_3=image_3*255
        return image_3
    
    # Image multiply mode
    def divide(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1/image_2
        image_3=image_3*255
        return image_3
    
    
    # Image multiply mode
    def screen(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=1-(1-image_1)*(1-image_2)
        image_3=image_3*255
        return image_3
    
                ################################ MAIN #################################
   
#Using blending_mode, apply a set of methods, and then display the results with matplotlib. 
def main():
    
    #read the images
    image_1 = cv2.imread('whats_heel.jpeg')
    image_2 = cv2.imread('whats_heel.jpeg')
    #create an object of the class
    blend = blending_mode()
    #apply the selected method
    result = blend.overlay(image_1,image_2)
    #display the result
    plt.imshow(result/255)
    plt.show()
    
    
    
if __name__ == '__main__':
    main()
  