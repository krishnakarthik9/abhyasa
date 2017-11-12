import numpy as np
import os
ones_file = os.listdir('./1')
file_size = len(ones_file)
count = 0
with open('file.txt') as f:
	f1=open('ones_to_train.txt', 'a')
    for line in f:
		if float(line) > 0.75:
			f1.write(ones_file[count]+'\n')
		count += 1
	f1.close()