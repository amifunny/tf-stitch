model.compile(optimizer='adam',
              loss = losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 10

history = model.fit( train_batches ,
                    epochs=epochs,
                    verbose=1)
