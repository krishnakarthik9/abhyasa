# abhyasa
Introduction to Machine Learning(CS771A) Course project. Team:Aravind, Gowtham, Abhishek, Harsha, Karthik


Kaggle Dataset:
https://drive.google.com/open?id=0B86eHLR6LlhEVjhWc19uUDFTSDg


python ml.py cnn train image
python ml.py cnn predict file


python file_generate_code.py 1  (will generate script_1.sh)
bash script_1.sh


python ml_version_2.py cnn train image
python ml_version_2.py cnn predict file



python predict_svm.py test/1



import os
os.listdir('./data')



Report:


Test accuracy for multiple batch sizes and num_epochs:

use ml_report.py setting batch_epoch to required value

run as python ml_report.py

check accuracy vs epochs plot for each if needed



Data Pruning:
	10 images of each class -> trained cnn and tested for extracted images(kaggle dataset) and increased each character from 10 to 28
	again 28 images for training the classifier and obtain new data


CNN Algorithm:

keras->optimizers->SGD for optimization

keras for CNN

Layer 1 -> POOL Layer -> ReLU activation

Layer 2 -> POOL Layer -> ReLU activation

Layer 3 -> POOL Layer -> ReLU activation

Layer 4 -> Fully Connected -> ReLU activation

finally softmax for linear classification(look at neural_network.py)

Hyper Parameters:

Batch Size for SGD

Number of epochs for SGD

GD parameters-lr,decay,momentum,nesterov??

CNN model descripton is saved to model.png


# Execution

* cd digitRecognition
* python3 track2.py kjhgfds.jpg
* When the image pops up, click 'Shift' button on the keyboard, output can be seen in the terminal


# Train the model

* cd src
* python ml.py cnn train image

# Existing Work

* In general, people use sliding window techniques for finding the labels


# Methodology:

* Write a mathematical expression in the sketchpad http://krishnakarthik.in/abhyasa/ and save the image
* Feed the image python3 track2.py kjhgfds.jpg for the latex expression
* Finding Contours
	- Using cv2.findContours, we obtain the contours (fresh_countours.png) 
	- We ignore the boxes with more than 60% of the area overlapping with other boxes (c108sigma_eliminate_inside_contours.png)
	- This is the final image (c108sigma_contours_final.png)
* Processing the boxes
	- Crop the boxes using PIL.Image's crop function and get rectangular images out of the boxes (_ppt17.png)
	- If height < width, will add (width-height)/2 on left and right sides of the image, which will then gives a squared image of (Height x Height)-(_sqrd17.png) and then use cv2.resize() to convert into 45x45 image(_small.png) - matplotlib import pyplot as plt for saving the image
	- We apply skeletonize() from skimage.morphology, for thinning the image - (output_17.png)
* Finding the Labels
	- Call the classifier and get the label with the highest probability
	- !,i,= -> these symbols have 2 parts, for these we have increased the height of the contour by 25% above and below, and then process the image again using the above techniques, and then classify the new boxes
* Locating the labels in the original image
	- Have a look at this example(beta_only.png), when we traverse through the boxes, sorted along the X-coordinate, a new character can assume many positions like superscript, subscript, on the same level,.. 
	- To handle this, we have considered characters to be nodes, with top, bottom, next, and parent attributes
	- And we recursively look for the level in which new character is going to be present
	- For this (beta_only.png) as input, we get this $ \sigma_{p}\beta_{3}^{k^{1}_{2}} $ expression as output
