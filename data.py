import os
import imageio
import nibabel as nib
from tqdm import trange
import cv2


currentPath = os.getcwd()
dataPath = currentPath + '/volumes'
labelPath = currentPath + '/labels'
trainImgPath = currentPath + '/data_test_all/images/train'
valImgPath = currentPath + '/data_test_all/images/val'
testImgPath = currentPath + '/data_test_all/images/test'
trainLabelPath = currentPath + '/ddata_test_all/labels/train'
valLabelPath = currentPath + '/data_test_all/labels/val'
testLabelPath = currentPath + '/data_test_all/labels/test'
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
'''
training: 58-139 / 43573
validation: 14-57 / 13127
test: 0-13 / 6803
'''
print("Training data...")

 # Images for Training
for fileNum in trange(10,15):
    os.chdir(dataPath)
    # Proxy 불러오기
    proxy = nib.load('volume-%d.nii.gz'%(fileNum)) # for Training and Testing images

    # 전체 Image array 불러오기
    arr = proxy.get_fdata()
    sliceNum = arr.shape[2]
    # if fileNum < 8:
    #     os.chdir(trainImgPath)
    # elif fileNum < 10:
    #     os.chdir(valImgPath)
    # elif fileNum < 15:
    #     os.chdir(testImgPath)
    os.chdir(valImgPath)
    for j in range(sliceNum):
        imageio.imwrite('image-%d-%d.png'%(fileNum, j), arr[:,:,j])
        
        

for fileNum in trange(10,15):
    os.chdir(labelPath)
    # Proxy 불러오기
    proxy = nib.load('labels-%d.nii.gz'%(fileNum)) # for Training and Testing images

    # 전체 Image array 불러오기
    arr = proxy.get_fdata()
    sliceNum = arr.shape[2]
    # if fileNum < 8:
    #     os.chdir(trainLabelPath)
    # elif fileNum < 10:
    #     os.chdir(valLabelPath)
    # elif fileNum < 15:
    #     os.chdir(testLabelPath)
    os.chdir(valLabelPath)
    for j in range(sliceNum):
        imageio.imwrite('image-%d-%d.png'%(fileNum, j), arr[:,:,j])
        # imageio.imwrite('image-%d-%d-clahe.png'%(fileNum, j), arr[:,:,j])

