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
			
			Example
			vision : Conv Model and CIFAR-10 DATASET
			nlp : Conv Model and IMDB Sentiment Analysis DATASET
			structure : DNN with Iris Datset

	model - Model to pre-construct
	dataset - Tensorflow dataset to use
	training - choose Training loop ,custom(default) or fit
	test : Whether to include test loop, true(default) or false
	preprocessing : Added by default for selected models
"""

def main():

	# Important features 
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
						help="domain problem type for selecting "+
							  "appropriate model and dataset"
						)

	parser.add_argument('--dataset',
						type=str,
						help="select any of Tensorflow datasets",
						required=False
						)

	parser.add_argument('--model',
						type=str,
						help="select the Deep Learning Model",
						required=False
						)

	parser.add_argument('--training',
						type=str,
						default="custom",
						help="type of training loop, Custom or built-in",
						required=False
						)

	parser.add_argument('--testing',
						type=bool,
						default=True,
						help="if to include testing",
						required=False
						)

	# Create a Namespace object of all arguments
	args = parser.parse_args()

	# Extension of the file name provided
	output_extension = os.path.splitext( args.output_file )[-1]

	if not (output_extension in ['.py','.ipynb']):
		raise( Exception( "Output File extension must be .py or .ipynb " ) )

	# Domain provided in argument
	domain = args.domain

	dataset = None
	model = None

	# Make sure either domain is provided,
	# or the choice of dataset and model
	if domain is None:

		if args.dataset==None or args.model==None :
			raise( Exception( "Either provide domain eg. -d = vision \n"+
				"or provide dataset and model eg. tf-stitch cifar-10 conv" ) )
		else :

			dataset = args.dataset
			model = args.model


	training = args.training	
	testing = args.testing	

	# Get template codes into `content_blocks`
	content_blocks = stitch_template( domain ,
									  dataset,
									  model,
									  training,
									  testing )

	# Write the file using `content_blocks`
	with open( args.output_file , "w" ) as file:

		if output_extension==".ipynb":

			notebook_json = stitch_notebook( content_blocks )
			json.dump( notebook_json , file )

		else:

			divide_columns = 80
			# Section divider for ".py" file to separate out code blocks
			section_divider = "#"+"-"*(divide_columns)
			# Two newlines between each code blocks and section divider
			file.write( ("\n\n"+section_divider+"\n\n").join( content_blocks ) )

		file.close()

	# Show in message at end of program.
	success_msg = "Your code is stitched to your fit. Thanks for Using :)"
	print( success_msg )

if __name__=='__main__':
	main()




