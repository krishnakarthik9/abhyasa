import os
batch_epoch=[[5,20],[32,20],[64,10],[64,20],[64,30]]
for batch,epoch in batch_epoch:
	print("running cnn for "+str(batch)+" "+str(epoch))
	os.system("python3 ml.py cnn train image "+str(batch)+" "+str(epoch))