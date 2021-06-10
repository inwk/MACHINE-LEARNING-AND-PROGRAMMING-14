# Deep Learning-Based Analysis of CT Images in Pancreatic Adenocarcinoma Patients

This project was conducted through machine learning and programming classes at Yonsei University.

## Table of Contents  

[1. Problem formulation](#1)
 * [1.1 Motivation](#11)
 * [1.2 Goal of project](#12)
 * [1.3 About prior study](#13)
 
[2. Dataset](#2)
 * [2.1 Public data](#21)
   * [2.1.1 Public data description](#211)
 * [2.2 Data preprocessing](#22)
 * [2.3 Data augmentation](#23)

[3. Models](#3)
 * [3.1 Semantic segmentation models](#31)
 * [3.2 U-NET](#32)
 * [3.3 DeepLabV3+](#33)

[4. Results](#4)
 * [4.1 Experimental results](#41)
 * [4.2 Segmented area quantification](#42)
 * [4.3 3d reconstruction](#43)

[5. Conclusion](#5)
 * [5.1 Analysis](#51)
 
[6. Future work](#6)
 * [6.1 Applying to read data](#61)
 * [6.2. 3d model](#62)

[7. How to use](#7)
 * [7.1 Setup](#71)
   * [7.1.1 Requirements](#711)
   * [7.1.2 Directory settings](#712)
 * [7.2 Training](#72)
 * [7.3 Evalutaion](#73)

[8. Reference](#8)

## Problem formulation <a name="1"></a>


* ### Motivation <a name="11"></a>

  Cancer cachexia is a multifactorial syndrome characterized by ongoing loss of skeletal muscle and fat. 

  Because pancreatic cancer patients with cachexia have much shorter survival time than those without cachexia, early diagnosis of cancer cachexia is crucial. Criteria for         cachexia include low BMI, extreme weight loss, and muscle/fat wasting. 

  While height, weight, and BMI are easily obtainable, muscle and fat mass requires more complicated analysis of a CT scan at the level of the third vertebra (L3).

  Therefore, if we develop an algorithm which can segment muscles and fat through ct images and calculate each mass and volume to diagnose cancer cachexia, it's a great help in    early diagnosis of cancer cachexia and, as a result, it's a great contribution to prolonging the lives of patients.

* ### Goal of project <a name="12"></a>
  Our goal of project is as follows. 

  1. Segment muscle and fat from CT images and compare with ground truth image
  2. Calculate each mass and volume 
  3. Developing an algorithm which can diagnose cancer cachexia from the segmented images and calculated mass and volume
  4. 
* ### About prior study <a name="13"></a>

  Prior to proceed with the project, prior studies were investigated.

## Dataset <a name="2"></a>


  Basically, segmentation tasks require ct images and corresponding labeled images. In addition, this project also requires information about mass and volumes for each segmented   class. 

  Since exportation of real data is not approved by IRB, we deciede to use public data instead.

* ### Public data <a name="21"></a>

  We decided to train a model via public dataset and apply our trained model to real data later.

  Public dataset was selected considering its similarity to real data.

  * #### Public data description <a name="211"></a>

    This dataset consists of 140 computed tomography (CT) scans, each with five organs labeled in 3D: lung, bones, liver, kidneys and bladder. The brain is also labeled on the       minority of scans which show it.

  Since the goal of our project is to segment two classes, we decided to use only two of the five classes in public dataset.

  About 7000 images were used for training and split by 7:2:1


  [Public Dataset Link](https://wiki.cancerimagingarchive.net/display/Public/CT-ORG%3A+CT+volumes+with+multiple+organ+segmentations)


* ### Data preprocessing <a name="22"></a>
  Since public data 
* ### Data Augmentation <a name="23"></a>
## Models <a name="3"></a>


* ### Semantic segmentation models <a name="31"></a>
* ### U-NET <a name="32"></a>
* ### DeepLabV3+ <a name="33"></a>
## Results <a name="4"></a>


* ### Experimental results <a name="41"></a>
* ### Segmented area quantification <a name="42"></a>
* ### 3D reconstrucition <a name="43"></a>
## Conclusion <a name="5"></a>


* ### Analysis <a name="51"></a>
## Future work <a name="6"></a>


* ### Applying to real data <a name="61"></a>
* ### 3D model <a name="62"></a>
## How to use <a name="7"></a>


* ### Setup <a name="71"></a>
*   #### Requirements <a name="711"></a>
*   #### Directory settings <a name="712"></a>
* ### Training <a name="72"></a>
* ### Evalutaion <a name="73"></a>
## Reference <a name="8"></a>



Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

- 📫 How to reach me **inwookoh@yonsei.ac.kr**


<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://opencv.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> </p>
