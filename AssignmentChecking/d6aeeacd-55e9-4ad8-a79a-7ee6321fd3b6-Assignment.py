

import numpy as np      #Import libraries 
import os
rootDir = 'photos'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
for fname in fileList:
    print('\t%s' % fname)
    print('Found directory: %s' % dirName)
file_count = sum([len(files) for r, d, files in os.walk("photos")])  #Count the number of files
print('Number of Files          :', file_count)
photos = np.zeros([20,200,200,3]) #create numpy array with (no of files, 200, 200, 3)

from PIL import Image          
def Resize(): #Resize function
    try: 
        #Relative Path 
        img = Image.open(rootDir)  
          
        #In-place modification 

        img = img.resize((20,200,200,3)) 
          
        img.save(rootDir) 
    except IOError: 
        pass
try:  
    img  = Image.open(rootDir)  
except IOError: 
    pass
def main():                    # Main function which returns array
    return(photos)
if __name__ == "__main__": 
    main()















