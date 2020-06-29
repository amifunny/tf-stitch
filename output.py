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
raw_data,info = tfds.load('mnist',split=['train','test'],with_info=True)

print(info)



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

@tf.function
def train_step(x, y):
    
    with tf.GradientTape() as tape:
        logits = model(x, training=True)
        loss_value = loss_fn(y, logits)
    
    grads = tape.gradient(loss_value, model.trainable_weights)
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    train_acc_metric.update_state(y, logits)
    
    return loss_value


epochs = 10

for epoch in range(epochs):

    start_time = time.time()

    # Iterate over the batches of the dataset.
    for step, (x_batch_train, y_batch_train) in enumerate(train_dataset):

        loss_value = train_step(x_batch_train, y_batch_train)

        # Log every 200 batches.
        if step % 200 == 0:
            print(
                "Training loss (for one batch) at step %d: %.4f"
                % (step, float(loss_value))
            )
            print("Seen so far: %d samples" % ((step + 1) * 64))

    # Display metrics at the end of each epoch.
    train_acc = train_acc_metric.result()
    print("Training acc over epoch: %.4f" % (float(train_acc),))

    # Reset training metrics at the end of each epoch
    train_acc_metric.reset_states()

    # Run a validation loop at the end of each epoch.
    for x_batch_val, y_batch_val in val_dataset:
        test_step(x_batch_val, y_batch_val)

    val_acc = val_acc_metric.result()
    val_acc_metric.reset_states()
    print("Validation acc: %.4f" % (float(val_acc),))
    print("Time taken: %.2fs" % (time.time() - start_time))



