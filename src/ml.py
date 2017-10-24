from data_loader import Data_Loader
# from svm import SVM
from cnn1 import CNN1
import numpy as np
import sys

def main():
	# print("something")
	ml_algorithm=sys.argv[1]
	ml_step=sys.argv[2]
	data_path = './data'
	test_size_ratio = 0.1
	loader = Data_Loader(data_path)
	# unshuffled split of data to train and test
	[train_img, train_labels, test_img, test_labels] = [np.array(x) for x in loader.load_all_data(test_size_ratio)]
	if ml_algorithm == "svm":
		svm_classifier = SVM(train_img, train_labels, test_img, test_labels)
		svm_classifier.plots()
	elif ml_algorithm == "cnn":
		cnn_classifier = CNN1(train_img, train_labels, test_img, test_labels)
		if ml_step=="test":
			accuracy=cnn_classifier.test()
		elif ml_step=="train":
			accuracy=cnn_classifier.train()
		return accuracy
if __name__ == '__main__':
	# print("something")
	accuracy=main()
	print(accuracy)
