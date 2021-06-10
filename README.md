# Deep Learning-Based Analysis of CT Images in Pancreatic Adenocarcinoma Patients

This project was conducted through machine learning and programming classes at Yonsei University.

## Problem formulation

### Motivation

Cancer cachexia is a multifactorial syndrome characterized by ongoing loss of skeletal muscle and fat. 

Because pancreatic cancer patients with cachexia have much shorter survival time than those without cachexia, early diagnosis of cancer cachexia is crucial. Criteria for cachexia include low BMI, extreme weight loss, and muscle/fat wasting. 

While height, weight, and BMI are easily obtainable, muscle and fat mass requires more complicated analysis of a CT scan at the level of the third vertebra (L3).

Therefore, if we develop an algorithm which can segment muscles and fat through ct images and calculate each mass and volume to diagnose cancer cachexia, it's a great help in early diagnosis of cancer cachexia and, as a result, it's a great contribution to prolonging the lives of patients.

### Goal of project

Our goal of project is as follows. 

1. Segment muscle and fat from CT images and compare with ground truth image
2. Calculate each mass and volume 
3. Developing an algorithm which can diagnose cancer cachexia from the segmented images and calculated mass and volume
### About prior study

Prior to proceed with the project, prior studies were investigated.

## Dataset

Basically, segmentation tasks require ct images and corresponding labeled images. In addition, this project also requires information about mass and volumes for each segmented class. 

Since exportation of real data is not approved by IRB, we deciede to use public data instead.

### Public data

We decided to train a model via public dataset and apply our trained model to real data later.

Public dataset was selected considering its similarity to real data.

#### Public data description

This dataset consists of 140 computed tomography (CT) scans, each with five organs labeled in 3D: lung, bones, liver, kidneys and bladder. The brain is also labeled on the minority of scans which show it.

Since the goal of our project is to segment two classes, we decided to use only two of the five classes in public dataset.

About 7000 images were used for training and split by 7:2:1

[Public Dataset Link](https://wiki.cancerimagingarchive.net/display/Public/CT-ORG%3A+CT+volumes+with+multiple+organ+segmentations)


### Data preprocessing
### Data Augmentation
## Models
### Semantic segmentation models
### U-NET
### DeepLabV3+
## How to use
## Results
### Experimental results
### Segmented area quantification
### 3D reconstrucition
## Conclusion
### Analysis
## Future work
### Applying to real data
### 3D model

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
