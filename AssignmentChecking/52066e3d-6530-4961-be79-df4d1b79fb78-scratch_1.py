import numpy as np
import matplotlib.pylab as plt
import os
import PIL
from PIL import Image
def main():
    photos = np.zeros([20, 512, 512, 3])
    rootDir = "photos/"
    ext = ".png"
    fnames = []
    i = 0
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            fnames.append(fname)
            img = Image.open(rootDir + fname)
            img = img.resize((512, 512), PIL.Image.ANTIALIAS)
            img = img.convert("RGB")
            img.save("Resized-Photos/" + fname + "resized" + ext)
            im = plt.imread("Resized-Photos/" + fname + "resized.png")
            photos[i] = im
            i = i+1
    for image in photos:
        return image[:]


if __name__ == "__main__":
    main()
