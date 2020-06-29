class ArgumentError(Exception):

	def __init__(self, argument , options):
		self.argument = argument
		self.options = options
		super().__init__(self.argument,self.options)

	def __str__(self):
		error_msg = "Invalid argument for `{}`\n".format(self.argument)
		option_msg = "Available options -> {}".format(self.options)
		return error_msg+option_msg


def get_files(**kwargs):

	with open('template.json',"rb") as file:
		json_dict = json.loads( file.read() )
		file.close()

	template_files = {}

	if not (kwargs.domain in json_dict.domain.keys) and not kwargs.domain==None:
		raise( ArgumentError("domain",json_dict.domain.keys) )

	cata_link = 'https://www.tensorflow.org/datasets/catalog/overview'
	print("Using dataset : {}. Check official catalogue at {}".format(kwargs.dataset,cata_link))

	template_files['import_file'] = json_dict.imports
	template_files['dataset_file'] = json_dict.dataset

	if not (kwargs.model in json_dict.model.keys):
		raise( ArgumentError("model",json_dict.domain.keys) )
	

	template_files['model_file'] = json_dict.model.(kwargs.model)

	if not (kwargs.training in json_dict.training.keys):
		raise( ArgumentError("training",json_dict.domain.keys) )

	template_files['training_file'] = json_dict.training.(kwargs.training)

	if kwargs.testing:
		template_files['testing_file'] = json_dict.testing

		return template_files

def stitch_template( domain=None,
					 dataset=None,
					 model=None,
					 training=None,
					 testing=None
					  ):

	files = get_files( domain,
					   dataset,
					   model,
					   training,
					   testing )

	template_content = []

	with open( 'templates/imports/'+files.import_file , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	with open( 'templates/dataset/'+files.dataset_file , "r" ) as file:
		template_content.append( file.read().strip().replace(%DATASET_NAME%,dataset) )
		file.close()

	with open( 'templates/model/'+files.model_file , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()	

	with open( 'templates/training/'+files.training_file , "r" ) as file:
		template_content.append( file.read().strip() )
		file.close()

	if file.training!=None:
		with open( 'templates/training/'+files.training_file , "r" ) as file:
			template_content.append( file.read().strip() )
			file.close()

	return template_content
