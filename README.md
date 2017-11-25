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


