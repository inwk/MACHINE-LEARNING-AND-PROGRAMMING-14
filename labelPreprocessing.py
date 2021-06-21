import os
import imageio
import nibabel as nib
import glob
import cv2
from PIL import Image
import numpy as np

currentPath = os.getcwd()
testPath = currentPath + '/test/123/labels/*.png'
trainLabelPath = currentPath + '/data_test_all/labels/train/*.png'
valLabelPath = currentPath + '/data_test_all/labels/val/*.png'
testLabelPath = currentPath + '/data_test_all/labels/test/*.png'

trainLabelFiles = glob.glob(trainLabelPath)
valLabelFiles = glob.glob(valLabelPath)
testLabelFiles = glob.glob(testLabelPath)
testFiles = glob.glob(testPath)

for f in trainLabelFiles:
    title, ext = os.path.splitext(f)

    img = Image.open(f)
    img = img.resize((256,256), Image.NEAREST)
    img = np.array(img, dtype=np.uint8)
    # print(title)
    img[img == 102] = 0
    img[img == 204] = 0
    img[img == 212] = 0
    img[img == 127] = 0
    img[img == 255] = 0
    img[img == 153] = 2
    img[img == 51] = 1

    class0Num = np.count_nonzero(img==0)
    class1Num = np.count_nonzero(img==1)
    class2Num = np.count_nonzero(img==2)
    class3Num = np.count_nonzero(img==3)
    class4Num = np.count_nonzero(img==4)
    class5Num = np.count_nonzero(img==5)

    pixelNum = class0Num+class1Num+class2Num+class3Num+class4Num+class5Num
    if pixelNum != 256*256:
        print(title)
        print(pixelNum)

    img = Image.fromarray(img)
    img.save(title+ext)

for f in valLabelFiles:
    title, ext = os.path.splitext(f)

    img = Image.open(f)
    img = img.resize((256,256),Image.NEAREST)
    img = np.array(img, dtype=np.uint8)
    # print(title)
    img[img == 102] = 0
    img[img == 204] = 0
    img[img == 212] = 0
    img[img == 255] = 0
    img[img == 153] = 2
    img[img == 51] = 1

    class0Num = np.count_nonzero(img==0)
    class1Num = np.count_nonzero(img==1)
    class2Num = np.count_nonzero(img==2)
    class3Num = np.count_nonzero(img==3)
    class4Num = np.count_nonzero(img==4)
    class5Num = np.count_nonzero(img==5)

    pixelNum = class0Num+class1Num+class2Num+class3Num+class4Num+class5Num
    if pixelNum != 256*256:
        print(pixelNum)

    img = Image.fromarray(img)
    img.save(title+ext)

for f in testLabelFiles:
    title, ext = os.path.splitext(f)

    img = Image.open(f)
    img = img.resize((256,256),Image.NEAREST)
    img = np.array(img, dtype=np.uint8)
    # print(title)
    img[img == 102] = 0
    img[img == 204] = 0
    img[img == 212] = 0
    img[img == 255] = 0
    img[img == 153] = 2
    img[img == 51] = 1

    class0Num = np.count_nonzero(img==0)
    class1Num = np.count_nonzero(img==1)
    class2Num = np.count_nonzero(img==2)
    class3Num = np.count_nonzero(img==3)
    class4Num = np.count_nonzero(img==4)
    class5Num = np.count_nonzero(img==5)

    pixelNum = class0Num+class1Num+class2Num+class3Num+class4Num+class5Num
    if pixelNum != 256*256:
        print(pixelNum)

    img = Image.fromarray(img)
    img.save(title+ext)

