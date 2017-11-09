import numpy as np
import cv2
from cnn import CNN
from keras.utils import np_utils
from keras import optimizers
import os
from PIL import Image 
import numpy as np
def predict(self,test_img):
		img_rows,img_columns = 45,45
		count = 0
		label_map={}
		for folder in os.listdir("/home/harsha/Desktop/7th_sem/cs771/project/extracted_images/"):
			label_map[folder]=count
			count+=1
		total_classes = count
		clf = CNN().build(img_rows,img_columns,1,total_classes,'model.h5')
		probs = clf.predict(test_img)
		# return probs
		prediction = probs.argmax(axis=1)
		return prediction