import numpy as np
import sys
import os

ones_file = os.listdir('./1')
file_size = len(ones_file)
count = 0
# with open('file.txt') as f:
# 	f1=open('ones_to_train.txt', 'a')
#     for line in f:
# 		if float(line) > 0.75:
# 			f1.write(ones_file[count]+'\n')
# 		count += 1
# 	f1.close()
f1 = open('script.sh','a')
while count < file_size:
	f1.write('python ml_version_2.py cnn predict file '+str(count)+'\n')
	if count + 50 < file_size:
		count = count+50
	else:
		break
f1.close()