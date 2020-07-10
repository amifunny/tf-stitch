train_data, test_data = raw_data['train'], raw_data['test']
# 'info' has a encoder that take care of
# tokenizing and getting vocabulary
encoder = info.features['text'].encoder
print('Vocabulary size: {}'.format(encoder.vocab_size))

# Check how will sequences be 
sample_string = 'Tf stitch is great.'

encoded_string = encoder.encode(sample_string)
print('Encoded string is {}'.format(encoded_string))

original_string = encoder.decode(encoded_string)
print('The original string: "{}"'.format(original_string))

BUFFER_SIZE = 10000
BATCH_SIZE = 64

train_data = train_dataset.shuffle(BUFFER_SIZE)

train_batches = train_dataset.padded_batch(BATCH_SIZE)
test_batches = test_dataset.padded_batch(BATCH_SIZE)