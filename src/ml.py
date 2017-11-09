from data_loader import Data_Loader
from svm import SVM
from cnn1 import CNN1
import PIL
import numpy as np
from PIL import Image
import sys
import os

def main():
	# print("something")
	ml_algorithm=sys.argv[1] #cnn or svm
	ml_step=sys.argv[2] #train or test
	data_format=sys.argv[3] #image or file
	data_path = '/home/harsha/Desktop/7th_sem/cs771/project/extracted_images'
	test_size_ratio = 0.1
	loader = Data_Loader(data_path)
	# unshuffled split of data to train and test
	class_data_count=1000
	#[train_img, train_labels, test_img, test_labels] = [np.array(x) for x in loader.load_all_data(test_size_ratio,data_format,class_data_count)]

	if ml_algorithm == "svm":
		svm_classifier = SVM(train_img, train_labels, test_img, test_labels)
		svm_classifier.plots()
	elif ml_algorithm == "cnn":
		print("starting CNN!")
		# cnn_classifier = CNN1().(train_img, train_labels, test_img, test_labels)
		if ml_step=="test":
			accuracy=cnn_classifier.test()
		elif ml_step=="train":
			accuracy=cnn_classifier.train()
		elif ml_step=="predict":
			file_path="test1.jpg"
			img = np.asarray(Image.open(file_path).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
			features=[]
			features.append(img/255.0)
			test_img=np.array(features)
			# print(test_img.shape)
			img_rows,img_columns=45,45
			test_data = test_img.reshape((test_img.shape[0], img_rows,img_columns))
			test_data = test_data[:, np.newaxis, :, :]
			# print(test_data.shape)
			prediction=CNN1().predict(test_data[np.newaxis,0])
			count = 0
			feature_map={}
			for folder in os.listdir("/home/harsha/Desktop/7th_sem/cs771/project/extracted_images"):
				# print(folder+":"+str(count))
				feature_map[count]=folder
				count+=1
			print(feature_map[prediction[0]])
		return
if __name__ == '__main__':
	# print("something")
	main()
	# print(accuracy)
