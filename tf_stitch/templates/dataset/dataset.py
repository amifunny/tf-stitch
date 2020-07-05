import tensorflow_datasets as tfds
raw_data,info = tfds.load( %DATASET_NAME% , split=['train','test'] , with_info=True)

print(info)