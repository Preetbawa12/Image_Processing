#!/usr/bin/env python
# coding: utf-8

# ## LAPLACIAN FILTER PROJECT ASSIGNMENT CODE

# #### IMPORTING  LIBRARIES

# In[3]:


import cv2                            ### Computer Vision Library for Filtering
from os import listdir                ### reading dataset from directory
from matplotlib import image          ### For reading image
import matplotlib.pyplot as plt       ### For Visualzation of image 


# #### LOAD DATASET FROM GIVEN PATH 

# In[4]:


loaded_images = list()                                        ### create an empty list to store images data
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  ### set path of dataset 
for filename in listdir(dataset_path):                        ### using loop to read images inside dataset
    img_data = image.imread(dataset_path + filename)          ### now, reading images step by step
    loaded_images.append(img_data)                            ###  move all images to above created empty list 
    print('> loaded %s %s' % (filename, img_data.shape))      ###  filename and shape of images
    #plt.axis("off")                                           ###  remvoing axis of image to display it more clearly
    #plt.imshow(img_data)                                      ### displaying images 1 by 1
    #plt.show()                                                ### use when display only images not detail about images


# #### APPLYING SPATIAL FILTER (MEDIAN FILTER) 

# In[9]:


loaded_images = list()                                        
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  
for filename in listdir(dataset_path):                        
    img_data = image.imread(dataset_path + filename)          
    med_filter = cv2.medianBlur(img_data, 3)                      
    loaded_images.append(med_filter)                           
    print('> loaded %s %s' % (med_filter,med_filter.shape))          
    #plt.axis("off")                                           
    #plt.imshow(gray, cmap = "gray")                          
    #plt.show()                                                


# ####  CANNY FILTER (Edge Detection)

# In[16]:


loaded_images = list()                                        
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  
for filename in listdir(dataset_path):                       
    img_data = image.imread(dataset_path + filename)          
    can  = cv2.Canny(img_data, 100,200)                     
    loaded_images.append(can)                                 
    print('> loaded %s %s' % (filename, can.shape))           
    #plt.axis("off")                                          
    #plt.imshow(lap, cmap = "gray")                          
    #plt.show()                                               


# ####  SOBEL FILTER (Edge Detection)  

# In[17]:


loaded_images = list()                                       
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  
for filename in listdir(dataset_path):                        
    img_data = image.imread(dataset_path + filename)          
    sobelx = cv2.Sobel(img_data,cv2.CV_64F,1,0,ksize=5)                      
    loaded_images.append(sobelx)                                 
    print('> loaded %s %s' % (filename, sobelx.shape))           
    #plt.axis("off")                                         
    #plt.imshow(lap, cmap = "gray")                           
    #plt.show()                                              


# #### APPLY LAPLACIAN FILTER ON IMAGES DATASET DIRECTLY TO VIEW RESULTS

# In[8]:


loaded_images = list()                                        
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                 
for filename in listdir(dataset_path):                       
    img_data = image.imread(dataset_path + filename)          
    lap  = cv2.Laplacian(img_data,cv2.CV_64F)                     ### applying Laplacian Filter on images
    loaded_images.append(lap)                                 
    print('> loaded %s %s' % (filename, lap.shape))           
    #plt.axis("off")                                          
    #plt.imshow(lap, cmap = "gray")                          
    #plt.show()                                               


# #### NOTE:: 

# in above code, the results of applying laplacian filter directly on gray images can be seen which highlight edges inside an image but it removes some important scene of the image. Laplacian filter works perfectly only for important edge features but it does not gives good results for all edge features of an image.  

# How to overcome this issue?
# first apply Guassian Filter to remove noise from images.Then, apply laplacian filter on guassian image. 

# ### Apply Laplacian Of Guassian Filter on image to imporve performance 

# #### 1 - APPLY GUASSIAN FILTER ON GRAY IMAGES DATASET

# In[11]:


loaded_images = list()                                        
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  
for filename in listdir(dataset_path):                        
    img_data = image.imread(dataset_path + filename)          
    guassian =cv2.GaussianBlur(img_data,(5,5),0)                  ### applying guassian filter on images
    loaded_images.append(guassian)                            
    print('> loaded %s %s' % (filename, guassian.shape))     
    #plt.axis("off")                                         
    #plt.imshow(guassian, cmap = "gray")                      
    #plt.show()                                               


# #### 2 - APPLY LAPLACIAN FILTER ON GUASSIAN IMAGE DATASET 

# In[13]:


loaded_images = list()                                       
dataset_path = 'C:\\Users\\PREET\\Data_set\\'                  
for filename in listdir(dataset_path):                        
    img_data = image.imread(dataset_path + filename)          
    guassian =cv2.GaussianBlur(img_data,(5,5),0)                  ###  applying guassian filter on images
    lap  = cv2.Laplacian(guassian,cv2.CV_64F)                
    loaded_images.append(lap)                                
    print('> loaded %s %s' % (filename, lap.shape))           
    #plt.axis("off")                                         
    #plt.imshow(lap, cmap = "gray")                          
    #plt.show()                                               


#  applying Laplacian filter on Gussian images gives much better result than applying directly on an image. 

# #### References

# https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202
