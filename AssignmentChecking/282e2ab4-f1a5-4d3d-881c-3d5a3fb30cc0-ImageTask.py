
import matplotlib.pylab as plt
import os
import numpy as np
from PIL import Image
rootdir = 'photos/'
size = 200, 200, 3

def create_array():
    photos = np.zeros([20, 200, 200, 3])
    return photos

def resize_image(pic):
    img = Image.open(rootdir + pic)
    img.thumbnail(size, Image.ANTIALIAS)
    img.load()
    arr = np.asarray(img, dtype="int32")
    return arr

def process_image_to_array(arr,cntr):
    photos = create_array()
    try:
        photos[cntr] = arr
        cntr += 1
    except Exception as e:
        print(arr.shape, i, cntr, e)

def main():
    cntr = 0
    lst = []
    for i in os.listdir(rootdir):
        rimg = resize_image(i)
        if rimg.shape == (200, 200, 3):
            process_image_to_array(rimg,cntr)
            lst.append(i)
        else:
            print(rimg.shape, i, 'Not Loaded')
        cntr += 1
    for l in lst:
        print(l,'Loaded In Array')


if __name__ == "__main__":
    main()
