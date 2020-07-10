class CustomLayer(layers.Layer):
   
    def __init__(self, units=32):
        super(CustomLayer, self).__init__()
        self.units = units

    # Use shape of first input as `input_shape`
    # Weights are created when layer is first called
    def build(self, input_shape):
        
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            trainable=True,
        )
        self.b = self.add_weight(
            shape=(self.units,), trainable=True 
        )

    def call(self, inputs):
        
        # TODO : YOU CODE HERE

        return 


input_shape = ( 10, )

def get_model():

	inputs = layers.Input()

	out = CustomLayer()(inputs)

	# Define more layers here

	outputs = layers.Dense(10,activation="softmax")

    model = Model(inputs,outputs)
    return model

model = get_model()    


















