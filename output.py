"""
	Imports -
"""
# Tensorflow 2.x
import tensorflow as tf
from tensorflow.keras import *

# also for matrix computations
import numpy

# for viewing images and graphs
import matplotlib.pyplot as plt

import tensorflow_datasets as tfds
raw_data,info = tfds.load( IRIS , split=['train','test'] , with_info=True)

print(info)

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

model.compile(optimizer='adam',
              loss = losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 10

history = model.fit( train_batches ,
                    epochs=epochs,
                    verbose=1)

def test_error( model , test_batches ):

  test_acc = metrics.Accuracy()
  test_acc.reset_states()

  for (x_batch_test, y_batch_test) in test_batches:
     
    pred = model( x_batch_test )
    pred_argmax = tf.argmax( pred , -1 )

    test_acc.update_state( y_batch_test , pred_argmax )

  print("Test Accuracy is ==> {}".format( test_acc ) )

  return test_acc