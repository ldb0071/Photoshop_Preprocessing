#Importing libraries
import cv2 as cv2
import numpy as np 
import matplotlib.pyplot as plt

###################################################################################### BLENDING MODES ###########################################################################################################################
                
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
    
    # Image lighten mode
    def lighten(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.maximum(image_1,image_2)
        image_3=image_3*255
        return image_3
    
    # Image diffusion mode
    def diffusion(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-(2*image_1*image_2)
        image_3=image_3*255
        return image_3
    
    # Image overlay mode
    def overlay(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image soft_light mode
    def soft_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image hard_light mode
    def hard_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=2*image_1*image_2+(1-2*image_2)*(1-image_1)
        image_3=image_3*255
        return image_3
    
    # Image color_dodge mode
    def color_dodge(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1/(1-image_2)
        image_3=image_3*255
        return image_3
    
    # Image linear_burn mode
    def linear_burn(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-1
        image_3=image_3*255
        return image_3
    
    # Image color_burn mode
    def color_burn(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=1-(1-image_1)/(image_2)
        image_3=image_3*255
        return image_3
    
    # Image linear_dodge mode
    def linear_dodge(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2
        image_3=image_3*255
        return image_3
    
    # Image vivid_light mode
    def vivid_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where(image_2<0.5,1-(1-image_1)/(2*image_2),image_1/(2*(1-image_2)))
        image_3=image_3*255
        return image_3
    
    # Image pin_light mode
    def pin_light(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where(image_2<0.5,np.minimum(image_1,2*image_2),np.maximum(image_1,2*(image_2-0.5)))
        image_3=image_3*255
        return image_3
    
    # Image hard_mix mode
    def hard_mix(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.where((image_1+image_2)<1,0,1)
        image_3=image_3*255
        return image_3
    
    # Image difference mode
    def difference(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=np.abs(image_1-image_2)
        image_3=image_3*255
        return image_3
    
    # Image exclusion mode
    def exclusion(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1+image_2-2*image_1*image_2
        image_3=image_3*255
        return image_3
    
    # Image subtract mode
    def subtract(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1-image_2
        image_3=image_3*255
        return image_3
    
    # Image divide mode
    def divide(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=image_1/image_2
        image_3=image_3*255
        return image_3
    
    
    # Image screen mode
    def screen(self,image_1,image_2):
        image_1=image_1/255
        image_2=image_2/255
        image_3=1-(1-image_1)*(1-image_2)
        image_3=image_3*255
        return image_3
    
############################################################################# MAIN ####################################################################################################################################
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
  