# Input image size
image_dimensions = (32,32,3)

# Number of "Neurons" for Dense layers
dense_layers_dimensions = [256,128,64,32,10]

def get_model():

	inputs = layers.Input(image_dimensions)

	# Input Normalization
	out = layers.BatchNormalization()(inputs)

	for dims in dense_layers_dimensions[:-1]:
		layers.Dense( dims , activation="relu")

	outpus = layers.Dense( dense_layers_dimensions[-1] , activation="softmax" )

# Maps `inputs` to `outputs` to construct a model
model = Model(inputs,outputs)