Siddharth Vadgama
UTA ID-1001397508

RUNNING INSTRUCTION::

1. Jupyter notebook is attached with this submission. in the input cell put all the function calls with image path as parameter. For Example, soccer_analysis(FILE_PATH)

OR

2. 
Test cases is included in the main function. Assuming data directory is in the same directory as the script. 

Part 1: 

I checked if it is gif or not if it is then I converted it into jpg and then I created a mask and found if the pixels were connected or not. 

Part 2:

I used color filtering technique. I converted the image to HSV and then found the upper and lower limit for green color and created a mask and then used thresholding to find the field. and similar technique to find out red players and blue players. 

Part 3: 
I used edge detection technique to find out the mountain range and used thresholding to convert it into a binary image.


