train_data, test_data = raw_data['train'], raw_data['test']

IMG_SIZE = 32 # All images will be resized to 32x32

def map_func(image, label):
  image = tf.cast(image, tf.float32)
  # Normalize image to be between [-1,1]
  image = (image/127.5) - 1
  # Resize all image to be of right dimension
  image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
  return image, label

train_data = train_data.map(map_func)
test_data = test_data.map(map_func)

BATCH_SIZE = 64
SHUFFLE_BUFFER_SIZE = 1000

train_batches = train_data.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
test_batches = test_data.batch(BATCH_SIZE)
