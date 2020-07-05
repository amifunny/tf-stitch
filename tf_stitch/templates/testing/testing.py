def test_error( model , test_batches ):

  test_acc = metrics.Accuracy()
  test_acc.reset_states()

  for (x_batch_test, y_batch_test) in test_batches:
     
    pred = model( x_batch_test )
    pred_argmax = tf.argmax( pred , -1 )

    test_acc.update_state( y_batch_test , pred_argmax )

  print("Test Accuracy is ==> {}".format( test_acc ) )

  return test_acc