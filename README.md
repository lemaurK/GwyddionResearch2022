![UTA-DataScience-Logo](https://user-images.githubusercontent.com/89792487/208189079-d4fc4d67-01bc-4397-891e-52f05330eb12.png)

# GwyddionResearch2022

### Hello researchers! 
This github repository functions as a hub for all iterations of code required to conduct cross sectional grain analysis from AFM images using Gwyddion analytical sofware and a bit of python.

First, you will need to install Gwyddion 32 bit version [here](https://sourceforge.net/projects/gwyddion/files/gwyddion/2.62/Gwyddion-2.62.win32.exe/download).

You will need the 32 bit version in order to utilize [Pygwy Scripting](http://gwyddion.net/documentation/user-guide-en/pygwy.html), which allows us to manipulate the software and extract pertinent data in one shot.
[Documentation](http://gwyddion.net/documentation/head/pygwy/) and the [forums](https://sourceforge.net/p/gwyddion/discussion/) for Gwyddion and Pygwy Scripting will come in handy in a pinch.

You will also need to install the latest version of [Python3](https://www.python.org/downloads/) and [Python2.7](https://www.python.org/downloads/release/python-2718/)

Just in case you have any trouble getting the Pygwy Console in Gwyddion to appear under the *Data Process* field [this](https://sourceforge.net/p/gwyddion/discussion/pygwy/thread/75317bfd11/) forum thread should help.

### After,
you are able to complete the instructions above we can move on to the code and some sample data.

Install wsl2 [Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#2-install-wsl) to use Jupyter Notebooks. This link is 



# GwyddionResearch2022

### Hello researchers! 
* This github repository functions as a hub for all iterations of code required to conduct cross sectional grain analysis from AFM images using Gwyddion analytical sofware and a bit of python.

## Overview

  The purpose for the task above is to provide a quantitatively supported description of the growth rate of the samples represented in the AFM images. Being able to define a growth rate for a reaction has many important applications that can be built on, resulting in unique findings. Defining a growth rate, for this specific application, involves analyzing relative maxima/minima of cross sections sliced from a scan. Making statistical calculations such as averages and standard deviations are also paramount to reliable growth rates.

## Summary of Work Done

### Data

* Gwyddion Data
  * Type: AFM Images 
    * Exported data: CSV containing matrix of height values (z-values) with dimensions N x N reflecting the size of the inital scan 
  * Size (512px x 512px image for example): 4600KB
  

#### Peek at Data

* Sample AFM Scan 


![image](https://user-images.githubusercontent.com/89792487/212432540-05ced332-745d-42fc-bdb3-939de5e49fca.png)

* Crossection of above white line


![image](https://user-images.githubusercontent.com/89792487/212432672-36cc6c40-362b-4877-9783-e73c8fdedfa6.png)

* Exported matrix of cross-sectional height data


![image](https://user-images.githubusercontent.com/89792487/212433676-0b648f85-595f-4275-bfa4-a449eabb1c6b.png)


#### Preprocessing / Clean up

* Defined in Python scripts...


### Conclusions

* Given my attempts did not end in any comparable and inferable results, I will state that MLM pipelined with either the N-gram model or the Word Distance Statistics (WDS) to locate the missing word would be the most effective route.

### Future Work

* Next steps would be to take another stab at integrating the missing word locating models into the picture and look more into HuggingFace's pretrained embedders.

## How to reproduce results

*Results in their current state are not ideal to reproduce.*

### Overview of files in repository

* MLM with Bert and HuggingFace Directory contains the script for respective model.
* MLM with Bert Directory contains the script for the respective model and the model file.
* NWP BI-LSTM Directory (Next Word Prediction BI-LSTM) contains the script for the respective model.

* Note that all of these notebooks should contain enough text for someone to understand what is happening.

### Software Setup and Python Packages Required

* First, you will need to install Gwyddion 32 bit version [here](https://sourceforge.net/projects/gwyddion/files/gwyddion/2.62/Gwyddion-2.62.win32.exe/download).

* You will need the 32 bit version in order to utilize [Pygwy Scripting](http://gwyddion.net/documentation/user-guide-en/pygwy.html), which allows us to manipulate the software and extract pertinent data in one shot.
[Documentation](http://gwyddion.net/documentation/head/pygwy/) and the [forums](https://sourceforge.net/p/gwyddion/discussion/) for Gwyddion and Pygwy Scripting will come in handy in a pinch.

* You will also need to install the latest version of [Python3](https://www.python.org/downloads/) and [Python2.7](https://www.python.org/downloads/release/python-2718/)

* Just in case you have any trouble getting the Pygwy Console in Gwyddion to appear under the *Data Process* field [this](https://sourceforge.net/p/gwyddion/discussion/pygwy/thread/75317bfd11/) forum thread should help.

* Install wsl2 [Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#2-install-wsl) to use Jupyter Notebooks. This link is for Windows machines only.

#### Packages

* Pandas
* Numpy
* scipy


## Citations

* [Locating and Filling Missing Words in Sentences](https://stlong0521.github.io/20160305%20-%20Missing%20Word.html)
* [Using pre-trained word embeddings](https://keras.io/examples/nlp/pretrained_word_embeddings/)
* [End-to-end Masked Language Modeling with BERT](https://keras.io/examples/nlp/masked_language_modeling/)
* [Keras NLP](https://keras.io/keras_nlp/)
* [HuggingFace](https://huggingface.co/)
* [Next Word Prediction BI-LSTM](https://www.kaggle.com/code/ysthehurricane/next-word-prediction-bi-lstm-tutorial-easy-way)
* [Pinecone NLP](https://www.pinecone.io/learn/nlp/)
* [Tensorflow Hub Bert](https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3)
* [Training Bert](https://www.youtube.com/watch?v=R6hcxMMOrPE&ab_channel=JamesBriggs)
* [Building a Next Word Predictor in Tensorflow](https://towardsdatascience.com/building-a-next-word-predictor-in-tensorflow-e7e681d4f03f#:~:text=Next%20Word%20Prediction%20or%20what,or%20emails%20without%20realizing%20it.)
* [Reference Image 1](https://www.google.com/url?sa=i&url=https%3A%2F%2Famitness.com%2F2020%2F05%2Fself-supervised-learning-nlp%2F&psig=AOvVaw0qVYDZlt8NPJTjONk7RDqH&ust=1671124544064000&source=images&cd=vfe&ved=0CBAQjhxqFwoTCKDsl5nO-fsCFQAAAAAdAAAAABAJ)
