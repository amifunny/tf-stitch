
def stitch_template( domain , dataset ):

	template_content = []

	with open( 'templates/imports/imports.py' , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	with open( 'templates/dataset/dataset.py' , "r" ) as file:
		template_content.append( file.read().strip().replace(%DATASET_NAME%,dataset) )
		file.close()

	with open( 'templates/conv_model.py' , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()	

	with open( 'templates/custom_train.py' , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	return template_content

def get_dataset_dwnld_temp( DATASET_NAME ):

	data_str ="""

import tensorflow_datasets as tfds
raw_data,info = tfds.load('{}',split=['train','test'],with_info=True)

print(info)

""".format(DATASET_NAME)

	return data_str
