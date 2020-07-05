def log(file,msg):
    file.write(msg+"\n")
    return

loss_fn = losses.SparseCategoricalCrossentropy()
optimizer = optimizers.Adam()

@tf.function
def train_step(x, y):
    
    with tf.GradientTape() as tape:
        yhat = model(x, training=True)
        loss = loss_fn( y, yhat )
    
    grads = tape.gradient( loss , model.trainable_weights )
    optimizer.apply_gradients( zip(grads, model.trainable_weights) )
    acc_metric.update_state( y, yhat )
    
    return loss


epochs = 10
acc_metric = metrics.Accuracy()
mean_metric = metrics.Mean()

log_file = open( log_filename , "w+")

for epoch in range(epochs):

    # to count epoch time
    start_time = time.time()

    # Iterate over the batches of the dataset.
    for (x_batch_train, y_batch_train) in train_batches:

        loss_value = train_step(x_batch_train, y_batch_train)



    # Display metrics and write to file at the end of each epoch.
    train_acc = acc_metric.result()
    epoch_loss = loss_metric.result()

    train_log = "Training Acc. for epoch *{}* - > : %.4f".format(  float(train_acc) )
    loss_log = "Avg Loss for epoch *{}* - > : %.4f".format(  float(train_acc) )

    log( log_file , train_log )
    log( log_file , loss_log )

    # Reset training metrics at the end of each epoch
    acc_metric.reset_states()
    mean_metric.reset_states()

    time_log = "Time taken: %.2fs" % (time.time() - start_time)
    log(log_file,time_log)

log_file.close()