import argparse
from .stitch import stitch_template
import os
from .stitch_ipynb import stitch_notebook
import json

"""
Arguments to take :-
	name :- Name of the starter file to produce
			( .py or .ipynb extension only )

	domain : (Optional) Problem domain in dl,
			so to give appropriate models and data.

			vision : Conv Model and CIFAR-10 DATASET
			nlp : Conv Model and IMDB Sentiment Analysis DATASET
			structure : DNN with Iris Datset

	model - Model to pre-construct
	dataset - Tensorflow dataset to use
	training - custom(default) or fit
	test : true(default) or false

"""

def main():

	# Important features 
	# reqired = bool , True default 
	# allow_abbrev = True ,default
	parser = argparse.ArgumentParser(prog="tf-stitch",
									description="Starter code with best practices for different Deep Learning problems in one command.",
									epilog="Thanks for Using.")

	# Argument for file to be generated
	parser.add_argument('output_file',
						type=str,
						help="the output file with starter code"
						)

	# Argument
	parser.add_argument('-d',
						'--domain',
						type=str,
						help="domain problem type for selecting\
							  appropriate model and dataset"
						)

	parser.add_argument('--dataset',
						type=str,
						help="Select any of Tensorflow datasets",
						required=False
						)

	parser.add_argument('--model',
						type=str,
						help="Select the Deep Learning Model",
						required=False
						)

	parser.add_argument('--training',
						type=str,
						default="custom",
						help="Type of training loop, Custom or built-in",
						required=False
						)

	parser.add_argument('--testing',
						type=bool,
						default=True,
						help="if to include testing",
						required=False
						)

	args = parser.parse_args()
	print( type(args) )

	output_extension = os.path.splitext( args.output_file )[-1]

	if not (output_extension in ['.py','.ipynb']):
		raise( Exception( " Output File extension must be .py or .ipynb " ) )

	domain = args.domain

	dataset = None
	model = None

	# Make sure either domain is provided,
	# or the choice of dataset or model
	if domain is None:

		if args.dataset==None or args.model==None :
			raise( Exception( "Either provide domain eg. -d = vision \n"+
				"or provide dataset and model eg. tf-stitch cifar-10 conv" ) )
		else :

			dataset = args.dataset
			model = args.model


	training = args.training	
	testing = args.testing	

	content_blocks = stitch_template( domain ,
									  dataset,
									  model,
									  training,
									  testing )

	with open( args.output_file , "w" ) as file:

		if output_extension==".ipynb":

			notebook_json = stitch_notebook( content_blocks )
			json.dump( notebook_json , file )

		else:

			file.write( "\n\n".join( content_blocks ) )

		file.close()


if __name__=='__main__':
	main()




