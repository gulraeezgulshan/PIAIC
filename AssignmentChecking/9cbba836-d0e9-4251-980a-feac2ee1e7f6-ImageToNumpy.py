import matplotlib.pylab as plt
from PIL import Image
import os
import numpy as np

def count_number_of_files():
    try:
        path, dirs, files = next(os.walk("photos"))
        file_count = len(files)
        return file_count
    except:
        raise Exception("photos not found")
def resizeImages(array):
    rootDir = "photos"
    for dirName,subdirList,fileList in os.walk(rootDir):
        print("Found Directory: %s" % dirName)
        for fname in fileList:
            file_path = os.path.splitext(fname)
            outfile = file_path[0] + "_200x200" + file_path[1]
            if file_path[1] == ".jpg":
                new_width = 200
                new_height = 200
                im1 = Image.open(rootDir + "/" + fname)
                im2 = im1.resize((new_width, new_height), Image.ANTIALIAS)
                im2.save(rootDir + "/" + outfile,"JPEG")
                im3 = plt.imread(rootDir + "/" + outfile)
                array.append(im3)
            elif file_path[1] == ".png":
                new_width = 200
                new_height = 200
                im1 = Image.open(rootDir + "/" + fname)
                im2 = im1.resize((new_width, new_height), Image.ANTIALIAS)
                im2.save(rootDir + "/" + outfile,"PNG")
                im3 = plt.imread(rootDir + "/" + outfile)
                array.append(im3)
def convert_to_a_array(array,array1):
    for i in range(0,len(array1)):
            array[i] = array1[i]
def main():
   fileCount = count_number_of_files()
   resizedPhotos = np.zeros((fileCount,200,200,3))
   array = []
   resizeImages(array)
   convert_to_a_array(resizedPhotos,array)
if __name__ == "__main__":
    main()
