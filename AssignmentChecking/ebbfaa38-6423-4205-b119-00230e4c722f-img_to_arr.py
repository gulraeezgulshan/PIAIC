import numpy as np
import glob
from PIL import Image
import os.path
from os import path
import os
def Fetch_files():
    rootDir = 'photos'
    try:
        r=path.exists(rootDir)
        if r != True:
            raise IOError
    except IOError:
        print('directory not found!')
    else:
        for dirName, subdirList, fileList in os.walk(rootDir):
            print('Found directory: %s' % dirName)
            print('Found:', len(fileList), 'Files')
def Resize():
    fileList = glob.glob('photos/*.jpg')
    for file in fileList:
        image = Image.open(file)
        img = image.resize((200,200))
    x = np.array([np.array(img) for fname in fileList])
    print(x.shape)
def main():
    Fetch_files()
    Resize()



