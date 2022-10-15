import cv2 as cv2
import numpy as np 


###################################################################################### NOISE_GENERATOR ###########################################################################################################################

#create a class that contains all photoshop noise methodes
class noise_generater:
    
    def __init__(self):
        pass
    
    
    #A function that add gaussian noise to an image and return the image
    def gaussian_noise(self,image,mean,var):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a gaussian noise 
        gaussian_noise = np.random.normal(mean,var,image_copy.shape)
        #add the noise to the image 
        image_copy = image_copy + gaussian_noise
        #clip the values 
        image_copy = np.clip(image_copy,0,255)
        return image_copy
    
    
    
    #A function that add salt and pepper noise to an image and return the image
    def salt_and_pepper_noise(self,image,prob):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a salt and pepper noise 
        salt_and_pepper_noise = np.random.uniform(0,1,image_copy.shape)
        #add the noise to the image 
        image_copy[salt_and_pepper_noise < prob/2] = 0
        image_copy[salt_and_pepper_noise > 1 - prob/2] = 255
        return image_copy
    
    
    
    #A function that add speckle noise to an image and return the image
    def speckle_noise(self,image,mean,var):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a speckle noise 
        speckle_noise = np.random.normal(mean,var,image_copy.shape)
        #add the noise to the image 
        image_copy = image_copy + image_copy*speckle_noise
        #clip the values 
        image_copy = np.clip(image_copy,0,255)
        return image_copy
    
    
    
    #A function that add poisson noise to an image and return the image
    def poisson_noise(self,image):
        
        #create a copy of the image 
        image_copy = image.copy()
        #add the noise to the image 
        image_copy = np.random.poisson(image_copy)
        #clip the values 
        image_copy = np.clip(image_copy,0,255)
        return image_copy
    
    
    
    #A function that add laplace noise to an image and return the image
    def laplace_noise(self,image,mean,var):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a laplace noise 
        laplace_noise = np.random.laplace(mean,var,image_copy.shape)
        #add the noise to the image 
        image_copy = image_copy + laplace_noise
        #clip the values 
        image_copy = np.clip(image_copy,0,255)
        return image_copy
    
    
    
    #A function that add uniform noise to an image and return the image
    def uniform_noise(self,image,mean,var):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a uniform noise 
        uniform_noise = np.random.uniform(mean,var,image_copy.shape)
        #add the noise to the image 
        image_copy = image_copy + uniform_noise
        #clip the values 
        image_copy = np.clip(image_copy,0,255)
        return image_copy
    
############################################################################# MAIN ####################################################################################################################################
#main function that applies to all noise types in the noise generator class. 
def main():
    #create an object from noise generator class
    noise_generator = noise_generater()
    #read the image 
    image = cv2.imread("whats_heel.jpeg")
    #convert the image to gray scale 
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #apply gaussian noise to the image 
    gaussian_noise_image = noise_generator.gaussian_noise(image,0,0.1)
    #apply salt and pepper noise to the image 
    salt_and_pepper_noise_image = noise_generator.salt_and_pepper_noise(image,0.1)
    #apply speckle noise to the image 
    speckle_noise_image = noise_generator.speckle_noise(image,0,0.1)
    #apply poisson noise to the image 
    poisson_noise_image = noise_generator.poisson_noise(image)
    #apply laplace noise to the image 
    laplace_noise_image = noise_generator.laplace_noise(image,0,0.1)
    #apply uniform noise to the image 
    uniform_noise_image = noise_generator.uniform_noise(image,0,0.1)
    #show the image 
    cv2.imshow("image",image)
    cv2.imshow("gaussian_noise_image",gaussian_noise_image/255)
    cv2.imshow("salt_and_pepper_noise_image",salt_and_pepper_noise_image/255)
    cv2.imshow("speckle_noise_image",speckle_noise_image/255)
    cv2.imshow("poisson_noise_image",poisson_noise_image/255)
    cv2.imshow("laplace_noise_image",laplace_noise_image/255)
    cv2.imshow("uniform_noise_image",uniform_noise_image/255)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()