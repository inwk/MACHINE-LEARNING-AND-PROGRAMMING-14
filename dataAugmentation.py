import os
import imageio
import nibabel as nib
from tqdm import trange
import cv2
import argparse
import glob

def main():
    parser = argparse.ArgumentParser(description="Data Augmentation")
    parser.add_argument('--input_path', type=str,
                        required=True, 
                        help='path for raw data')
    parser.add_argument('--output_path', type=str,
                        required=True, 
                        help='path for where to save iamges')
    parser.add_argument('--clipLimit', type=float, default=2.0, 
                        help='clipLimit for CLAHE')    
    parser.add_argument('--tileGridSize', nargs='+', type=int, default=(8,8), 
                        help='tileGridSize for CLAHE ex) 8,8')    
    parser.add_argument('--clahe', action='store_true', default=False, 
                        help='data augmentation with clahe')
    parser.add_argument('--vflip', action='store_true', default=False, 
                        help='data augmentation with vflip')            

    args = parser.parse_args()

    # CLAHE Parmaeters
    clipLimit = args.clipLimit
    tileGridSize = (args.tileGridSize[0], args.tileGridSize[1])
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)              
    # Path                             
    dataRawPath = args.input_path
    dataSavePath = args.output_path
    dataRawFiles = glob.glob(dataRawPath+'/*.png')

    if os.path.isdir(dataSavePath)==False:
        os.mkdir(dataSavePath)

    for f in dataRawFiles:
        base = os.path.basename(f)
        title, ext = os.path.splitext(base)
        # print(title, ext)
        img = cv2.imread(f,0)
        cv2.imwrite(dataSavePath+'/'+title+ext,img)
        if args.clahe:
            img_clahe = clahe.apply(img)
            claheName = dataSavePath+'/'+title+'-clahe'+ext
            cv2.imwrite(claheName,img_clahe)

        if args.vflip:
            img_vflip = cv2.flip(img,0)
            vflipName = dataSavePath+'/'+title+'-vflip'+ext
            cv2.imwrite(vflipName,img_vflip)

if __name__ == "__main__":
   main()