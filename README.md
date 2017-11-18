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




import os
os.listdir('./data')



Report:
Data Pruning:
	10 images of each class -> trained cnn and tested for extracted images(kaggle dataset) and increased each character from 10 to 28
	again 28 images for training the classifier and obtain new data