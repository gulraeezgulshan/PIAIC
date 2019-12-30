

import os
import numpy as np
from PIL import Image


def rootdirset():
    rootDir = 'Photos'
    return rootDir

def file_count_find():
    filenames = next(os.walk(rootdirset()))[2]
    #path, dirs, files = next(os.walk(rootdirset()))
    fileCount = len(filenames)
    return fileCount

def default_array_create():
    array_of_images = np.zeros((file_count_find(),200,200,3))
    return array_of_images
    
def file_path():
    try:
        filenames = next(os.walk(rootdirset()))[2]
        return filenames
    except:
        print("Directory name is not ""Photos"" kindy change directory name Or Directory doesn't exist")

        
def image_resizing():
    try:
        file_name = file_path()
        main_array = default_array_create()
        for x in range(0,file_count_find()):
            img = Image.open(rootdirset()+"\\"+ file_name[x])
            resize_img = img.resize((200, 200))
            resize_arry = np.array(resize_img)
            main_array[x] = resize_arry
        print("Task Successfully Completed")
        return main_array
    except:
        print("Something wrong happened.")


def main():
    final_array = image_resizing()
    shape_of_array = final_array.shape
    print("\nFinal Shape of Array  :",shape_of_array)

if __name__ == "__main__":
    main()


