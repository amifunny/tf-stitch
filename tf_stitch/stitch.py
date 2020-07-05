import json
import os

# path of where package is installed in system
RES_PATH = os.path.dirname(__file__)+"\\"

# Exception class for producing message , if argument
# given by user is invalid and also showing valid possible 
# options.
class ArgumentError(Exception):

	def __init__(self, argument , options):
		# Argument that is invalid
		self.argument = argument
		# Valid options from read json files
		self.options = options
		super().__init__(self.argument,self.options)

	def __str__(self):
		error_msg = "Invalid argument for `{}`\n".format(self.argument)
		option_msg = "Available options -> [{}]".format( " ,".join(self.options) )
		# Combining both messages
		return error_msg+option_msg


def get_files(**kwargs):

	# 'template.json' file contains mapping of arguments,
	# to possible values and their corresponding template filenames
	with open(RES_PATH+'template.json',"rb") as file:
		json_dict = json.loads( file.read() )
		file.close()

	# To hold different parts of required template,
	# as key-value pair,
	# For `template_files['model_file]`="conv_model.py"
	template_files = {}


	# Conditions check if argument is one of the keys,
	# in json of that argument type
	# For eg. 'domain' argument given by user, should be one
    # of ['conv','rnn' .. etc] that are keys in .json file
    # under the 'domain' field.
    # See `template.json` for reference


	if not (kwargs['domain'] in json_dict['domain'].keys()) and not kwargs['domain']==None:
		raise( ArgumentError("domain",json_dict['domain'].keys()) )

	if kwargs['domain']!=None :
		kwargs['dataset'] = json_dict['domain'][kwargs['domain']]['dataset']
		kwargs['model'] = json_dict['domain'][kwargs['domain']]['model']


	# Prompt to ask user to view valid tensorflow dataset names,
	# by browsing the `cata_link`
	cata_link = 'https://www.tensorflow.org/datasets/catalog/overview'
	print("Using dataset : {}. Check official catalogue at {}".format(kwargs['dataset'],cata_link))

	# Currently there are not varing options for 
	# import and dataset part of template
	template_files['import_file'] = json_dict['imports']
	template_files['dataset_file'] = json_dict['dataset']

	# TODO : Add Preprocessing options as well.

	if not (kwargs['model'] in json_dict['model'].keys()):
		raise( ArgumentError("model",json_dict['domain'].keys()) )

	template_files['model_file'] = json_dict['model'][kwargs['model']]

	if not (kwargs['training'] in json_dict['training'].keys()):
		raise( ArgumentError("training",json_dict['domain'].keys() ) )

	template_files['training_file'] = json_dict['training'][kwargs['training']]

	# add template of testing if True
	if kwargs['testing']:
		template_files['testing_file'] = json_dict['testing']

	# Also return datset , that was either given or
	# determined by domain
	return template_files,kwargs['dataset']

def stitch_template( domain=None,
					 dataset=None,
					 model=None,
					 training=None,
					 testing=None
					  ):

	# Get the template files name according to user's argument
	files,dataset = get_files( domain=domain,
					   dataset=dataset,
					   model=model,
					   training=training,
					   testing=testing )

	# Store code blocks, read from template files
	template_content = []

	with open( RES_PATH+'templates/imports/'+files['import_file'] , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	# For dataset template part , a special keyword => '%DATASET_NAME%',
	# is used to replace it with provided or default dataset name.
	with open( RES_PATH+'templates/dataset/'+files['dataset_file'] , "r" ) as file:
		template_content.append( file.read().strip().replace('%DATASET_NAME%',dataset) )
		file.close()

	with open( RES_PATH+'templates/model/'+files['model_file'] , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()	

	with open( RES_PATH+'templates/training/'+files['training_file'] , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	if files['testing_file']!=None:
		with open( RES_PATH+'templates/testing/'+files['testing_file'] , "r" ) as file:
			template_content.append( file.read().strip() )
			file.close()

	return template_content
