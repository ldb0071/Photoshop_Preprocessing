import cv2 as cv2
import numpy as np

###################################################################################### COLOR_CHANNELS ###########################################################################################################################


class color_channel():
    
    
    def __init__(self):
       pass
   
   
    #A function that create solid color images
    def create_solid_color_image(width,height,rgb):
        
        image = np.zeros((height,width,3), np.uint8)
        print(image[:].shape)
        image[:] = rgb
        return image


    #A function that remove a color channel from an image
    def remove_color_channel(self,image,channel):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a list of color channels 
        channels = ['b','g','r']
        #remove the color channel 
        image_copy[:,:,channels.index(channel)] = 0
        return image_copy


    #A function that select a specific color channel from an image and return the image
    def select_color_channel(self,image,channel):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a list of color channels 
        channels = ['b','g','r']
        #check if the channel is b 
        if channel == 'b':
            #select the b channel 
            image_copy[:,:,1] = 0
            image_copy[:,:,2] = 0
            return image_copy
        #check if the channel is g 
        elif channel == 'g':
            #select the g channel 
            image_copy[:,:,0] = 0
            image_copy[:,:,2] = 0
            return image_copy
        #check if the channel is r 
        elif channel == 'r':
            #select the r channel 
            image_copy[:,:,0] = 0
            image_copy[:,:,1] = 0
            return image_copy
        else:
            print('please enter a valid channel')
            
            

    #A function that turn the image into any image color representation and return the image
    def color_representation(self,image,representation):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a list of color representations 
        representations = ['RGB','HSV','YUV','YIQ','YCbCr']
        #check if the representation is RGB 
        if representation == 'RGB':
            return image_copy
        #check if the representation is HSV 
        elif representation == 'HSV':
            #convert the image to HSV 
            image_copy = cv2.cvtColor(image_copy,cv2.COLOR_RGB2HSV)
            return image_copy
        #check if the representation is YUV 
        elif representation == 'YUV':
            #convert the image to YUV 
            image_copy = cv2.cvtColor(image_copy,cv2.COLOR_RGB2YUV)
            return image_copy
        #check if the representation is YIQ 
        elif representation == 'YIQ':
            #convert the image to YIQ 
            image_copy = cv2.cvtColor(image_copy,cv2.COLOR_RGB2YIQ)
            return image_copy
        #check if the representation is YCbCr 
        elif representation == 'YCbCr':
            #convert the image to YCbCr 
            image_copy = cv2.cvtColor(image_copy,cv2.COLOR_RGB2YCrCb)
            return image_copy
        else:
            print('please enter a valid representation')
            


    #A function that change channels values in an image and return the image
    def change_channels_values(self,image,channels_values):
        
        #create a copy of the image 
        image_copy = image.copy()
        #create a list of color channels 
        channels = ['b','g','r']
        #change the channels values 
        for i in range(3):
            image_copy[:,:,i] = channels_values[i]
        return image_copy



    #A function that change image hue and saturation  and return the image
    def change_hue_saturation(self,image,hue,saturation):
        
        #create a copy of the image 
        image_copy = image.copy()
        #convert the image to HSV 
        image_copy = cv2.cvtColor(image_copy,cv2.COLOR_RGB2HSV)
        #change the hue and saturation 
        image_copy[:,:,0] = hue
        image_copy[:,:,1] = saturation
        #convert the image to RGB 
        image_copy = cv2.cvtColor(image_copy,cv2.COLOR_HSV2RGB)
        return image_copy
    
    
     #A function that apply a color balance effect 
    def color_balance(self,image,red,green,blue):
        #create a color balance effect 
        red = np.clip(red,-100,100)
        green = np.clip(green,-100,100)
        blue = np.clip(blue,-100,100)
        red = red/100
        green = green/100
        blue = blue/100
        image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        image[:,:,0] = image[:,:,0]*blue
        return image


############################################################################# MAIN ####################################################################################################################################
# apply the transformation to an image and display the image.

def main():
    
    #create an object from the class color_channel
    color_channel_object = color_channel()
    #read the image 
    image = cv2.imread('whats_heel.jpeg')
    #convert the image to RGB 
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    #create a solid color image 
    # solid_color_image = color_channel_object.create_solid_color_image(100,100,(255,0,0))
    #remove the red channel from the image 
    image_without_red_channel = color_channel_object.remove_color_channel(image,'r')
    #select the red channel from the image 
    image_red_channel = color_channel_object.select_color_channel(image,'r')
    #convert the image to HSV 
    image_hsv = color_channel_object.color_representation(image,'HSV')
    #change the channels values in the image 
    image_channels_values = color_channel_object.change_channels_values(image,[0,0,255])
    #change the hue and saturation in the image 
    image_hue_saturation = color_channel_object.change_hue_saturation(image,0,0)
    #create a list of images 
    images = [image,image_without_red_channel,image_red_channel,image_hsv,image_channels_values,image_hue_saturation]
    #create a list of titles 
    titles = ['original image','image without red channel','image red channel','image hsv','image channels values','image hue saturation']
    #loop through the images and titles 
    for i in range(len(images)):
        #display the image 
        cv2.imshow(titles[i],images[i])
    #wait for a key to be pressed 
    cv2.waitKey(0)
    #destroy all the windows 
    cv2.destroyAllWindows()



if __name__=='__main__':
    main()