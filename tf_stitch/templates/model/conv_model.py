# Input image size
image_dimensions = (32,32,3)

# Number of filter for Convolution layers
conv_layers_dimensions = [256,128,64,32]
# Number of "Neurons" for Dense layers
dense_layers_dimensions = [256,10]

def get_model():

	inputs = layers.Input(image_dimensions)

	# Input Normalization
	out = layers.BatchNormalization()(inputs)

	for dims in conv_layers_dimensions:
		out = layers.Conv(dims , (3,3) , activation="relu")(out)
		# Reduce heigth and width of each filter
		out = layers.MaxPool()(out)

	for dims in dense_layers_dimensions[:-1]:
		layers.Dense( dims , activation="relu")

	outputs = layers.Dense( dense_layers_dimensions[-1] , activation="softmax" )

	# Maps `inputs` to `outputs` to construct a model
	model = Model(inputs,outputs)
	return model

model = get_model()	