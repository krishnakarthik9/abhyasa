from data_loader import Data_Loader
# from svm import SVM
from cnn_version_2 import CNN1
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
	data_path = './data'
	test_size_ratio = 0.1
	loader = Data_Loader(data_path)
	# unshuffled split of data to train and test
	class_data_count=100
	[train_img, train_labels, test_img, test_labels] = [np.array(x) for x in loader.load_all_data(test_size_ratio,data_format,class_data_count)]

	if ml_algorithm == "svm":
		svm_classifier = SVM(train_img, train_labels, test_img, test_labels)
		svm_classifier.plots()
	elif ml_algorithm == "cnn":
		print("starting CNN!")
		cnn_classifier = CNN1(train_img, train_labels, test_img, test_labels)
		if ml_step=="test":
			accuracy=cnn_classifier.test()
		elif ml_step=="train":
			accuracy=cnn_classifier.train()
		elif ml_step=="predict":
			offset=int(sys.argv[5]) #image or file
			i = 0
			folder_name = sys.argv[4]
			file = os.listdir('./extracted_images/' + folder_name)
			file_size = len(file)
			training_list = []
			final_list = []
			while i < 20:
				img = np.asarray(Image.open('./extracted_images/'+folder_name+'/'+file[i+offset]).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
				features=[]
				features.append(img/255.0)
				test_img=np.array(features)
				# print(test_img.shape)
				img_rows,img_columns=45,45
				test_data = test_img.reshape((test_img.shape[0], img_rows,img_columns))
				test_data = test_data[:, np.newaxis, :, :]
				# print(test_data.shape)
				prediction,probability=cnn_classifier.predict(test_data[np.newaxis,0],folder_name)
				count = 0
				feature_map={}
				for folder in os.listdir("./data"):
					# print(folder+":"+str(count))
					feature_map[count]=folder
					count+=1
				print(feature_map[prediction[0]], i+offset, file[i+offset])
				if feature_map[prediction[0]] == folder_name:
					if probability > 0.6:
						final_list.append(file[i+offset])
				i = i+1;

			# _file = os.listdir('./extracted_images/'+folder_name)
			# file_size = len(_file)
			# count = 0
			# while count < 50:
			# 	if training_list[count] > 0.85:
			# 		final_list.append(_file[count])
			# 	count += 1
			f1 = open('final_images/final_'+folder_name+'.txt','a')
			f1.write('\n')
			f1.write('\n'.join(final_list))
			f1.close()
		return
if __name__ == '__main__':
	# print("something")
	main()
	# print(accuracy)
