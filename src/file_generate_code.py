import numpy as np
import sys
import os

folder_name = sys.argv[1]
_file = os.listdir('./extracted_images/'+folder_name)
file_size = len(_file)
count = 0
# with open('file.txt') as f:
# 	f1=open('ones_to_train.txt', 'a')
#     for line in f:
# 		if float(line) > 0.75:
# 			f1.write(ones_file[count]+'\n')
# 		count += 1
# 	f1.close()
f1 = open('script_'+folder_name+'.sh','a')
while count < file_size:
	f1.write('python ml_version_2.py cnn predict file '+sys.argv[1]+'\t'+str(count)+'\n')
	if count + 20 < file_size:
		count = count+20
	else:
		break
f1.close()