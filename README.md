![UTA-DataScience-Logo](https://user-images.githubusercontent.com/89792487/208189079-d4fc4d67-01bc-4397-891e-52f05330eb12.png)

# GwyddionResearch2022

### Hello researchers! 
* This github repository functions as a hub for all iterations of code required to conduct cross sectional grain analysis from AFM images using Gwyddion analytical sofware and a bit of python.

## Overview

  The purpose for the task above is to provide a quantitatively supported description of the growth rate of the samples represented in the AFM images. Being able to define a growth rate for a reaction has many important applications that can be built on, resulting in unique findings. Defining a growth rate, for this specific application, involves analyzing relative maxima/minima of cross sections sliced from a scan. Making statistical calculations such as averages and standard deviations are also paramount to reliable growth rates.

## Summary of Work Done

## Data

* Gwyddion Data
  * Type: AFM Images 
    * Exported Data: CSV containing matrix of height values (z-values) with dimensions N x N reflecting the size of the inital scan 
  * Size (512px x 512px image for example): 4600KB
  

## Peek at Data

* Sample AFM Scan 


![image](https://user-images.githubusercontent.com/89792487/212432540-05ced332-745d-42fc-bdb3-939de5e49fca.png)

* Crossection of above white line


![image](https://user-images.githubusercontent.com/89792487/212432672-36cc6c40-362b-4877-9783-e73c8fdedfa6.png)

* Exported matrix of cross-sectional height data


![image](https://user-images.githubusercontent.com/89792487/212433676-0b648f85-595f-4275-bfa4-a449eabb1c6b.png)


## Preprocessing / Clean up

*Explained in detail within documentation.*

## Conclusion

* Given that Gwyddion has plenty of analysis capabilities within the software, it was clear growth rate analysis would need to be conducted on its own. Through a series of developing, testing, and comparing the results of my python scripts I landed on a confident model worthy of implementation. There will always be room for improvement, however the structure of the codebase is tailored to be friendly to novices, with debugging capabilities included.

## Future Work

* Settle on a physical model that captures the appropriate mixture of physics and chemistry topics included in this experiment. Once a model is decided upon, create a simple script to add the curve to the final plots.

## How to reproduce results

*Explained in detail within documentation.*

## Overview of files in repository

* AFM Image Data
* Grain Analysis Jupyter Notebook Script
* Grain Analysis Python Script
* Pygwy Console Script

## Software Setup and Python Packages Required

* First, you will need to install Gwyddion 32 bit version [here](https://sourceforge.net/projects/gwyddion/files/gwyddion/2.62/Gwyddion-2.62.win32.exe/download).

* You will need the 32 bit version in order to utilize [Pygwy Scripting](http://gwyddion.net/documentation/user-guide-en/pygwy.html), which allows us to manipulate the software and extract pertinent data in one shot.
[Documentation](http://gwyddion.net/documentation/head/pygwy/) and the [forums](https://sourceforge.net/p/gwyddion/discussion/) for Gwyddion and Pygwy Scripting will come in handy in a pinch.

* You will also need to install the latest version of [Python3](https://www.python.org/downloads/) and [Python2.7](https://www.python.org/downloads/release/python-2718/)

* Just in case you have any trouble getting the Pygwy Console in Gwyddion to appear under the *Data Process* field [this](https://sourceforge.net/p/gwyddion/discussion/pygwy/thread/75317bfd11/) forum thread should help.

* Install wsl2 [Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#2-install-wsl) to use Jupyter Notebooks. This link is for Windows machines only.

## Python Packages

* Matplotlib
* Numpy
* scipy
* csv

## Citations

* [Leveling AFM Image](http://gwyddion.net/documentation/user-guide-en/leveling-and-background.html)
* [Gwyddion Color Map](http://gwyddion.net/documentation/user-guide-en/color-map.html)
* [Gwyddion Tools](http://gwyddion.net/documentation/user-guide-en/tools.html)
* [Pygwy Module](http://gwyddion.net/documentation/user-guide-en/pygwy.html)
* [Pygwy Head Function](http://gwyddion.net/documentation/head/pygwy/)

