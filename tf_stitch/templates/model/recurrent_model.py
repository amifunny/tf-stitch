# Input embedding
embedding_dimensions = 128

# Number of filter for Convolution layers
gru_layers_dimensions = [256,256]
# Number of "Neurons" for Dense layers
dense_layers_dimensions = [1]

def get_model():

	inputs = layers.Input((BATCH_SIZE,))

    out = layers.Embedding(encoder.vocab_size, embedding_dimensions )(inputs)

	for dims in gru_layers_dimensions[:-1]:
		out = layers.GRU( dims , return_sequences=True )(out)

	out = layers.GRU( gru_layers_dimensions[-1] )(out)

	for dims in dense_layers_dimensions[:-1]:
		layers.Dense( dims )

	outputs = layers.Dense( dense_layers_dimensions[-1] , activation="softmax" )

	# Maps `inputs` to `outputs` to construct a model
	model = Model(inputs,outputs)
	return model

model = get_model()	