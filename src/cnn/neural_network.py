from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.utils import plot_model
class CNN:
	def build(self, Width, Height, Depth, total_classes, Saved_Weights_Path=None):
		# Initialize the Model
		model = Sequential()

		# First CONV => RELU => POOL Layer
		model.add(Convolution2D(20, 5, 5, border_mode="same", input_shape=(Depth, Height, Width)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),dim_ordering="th"))
		# Second CONV => RELU => POOL Layer
		model.add(Convolution2D(50, 5, 5, border_mode="same",input_shape=(Depth, Height, Width)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),dim_ordering="th"))
		
		# Third CONV => RELU => POOL Layer 
		# Convolution -> ReLU Activation Function -> Pooling Layer
		model.add(Convolution2D(100, 5, 5, border_mode="same",input_shape=(Depth, Height, Width)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),dim_ordering="th"))

		# FC => RELU layers
		# Fully Connected Layer -> ReLU Activation Function
		model.add(Flatten())
		model.add(Dense(500))
		model.add(Activation("relu"))

		# Using Softmax Classifier for Linear Classification
		model.add(Dense(total_classes))
		model.add(Activation("softmax"))
		plot_model(model,show_shapes=True,to_file='model.png')

		# If the saved_weights file is already present i.e model is pre-trained, load that weights
		if Saved_Weights_Path is not None:
			model.load_weights(Saved_Weights_Path)
		return model