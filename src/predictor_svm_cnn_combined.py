from svm import SVM
from cnn1 import CNN1
import numpy as np
from PIL import Image
import os
import sys

def predict_label(img):
	svm_classifier = SVM()
	cnn_classifier = CNN1()
	probs_svm = svm_classifier.get_probs_svm([img])

	features=[]
	features.append(img/255.0)
	test_img=np.array(features)
	img_rows,img_columns=45,45
	test_data = test_img.reshape((test_img.shape[0], img_rows,img_columns))
	test_data = test_data[:, np.newaxis, :, :]
	probs_cnn = cnn_classifier.get_probs_cnn(test_data[np.newaxis,0])

	probs = (probs_svm + probs_cnn)/2.0
	feature_map={}
	count = 0
	for folder in os.listdir("./data"):
		# print(folder+":"+str(count))
		feature_map[count]=folder
		count+=1
	max_prob_index = probs[0].argmax(axis=0)
	print(probs[0])
	print(feature_map[max_prob_index], probs[0][max_prob_index], )
	
	count = 0
	for folder in os.listdir("./data"):
		# print(folder+":"+str(count))
		feature_map[count]=folder
		print(feature_map[count], '\t',probs_cnn[0][count], '\t',probs_svm[0][count], '\t',probs[0][count])
		count+=1

img = 'test/'+sys.argv[1]
predict_label(np.asarray(Image.open(img).convert('L').resize((45,45), Image.ANTIALIAS)).flatten())