import argparse
from stitch import stitch_template
import os
from stitch_ipynb import stitch_notebook
import json
"""
Arguments to take :-
	name :- Name of the starter file to produce
			( .py or .ipynb extension only )

	domain : (Optional) Problem domain in dl,
			so to give appropriate models and data.

			vision : Conv Model and CIFAR-10 DATASET
			nlp : Conv Model and IMDB Sentiment Analysis DATASET
			feature : DNN with HOUSE PRICING DATSET

	model - 
	dataset -
	training - custom(default) or fit
	test : true(default) or false
	logging : True(default) or False

"""
# Important features 
# reqired = bool , True default 
# allow_abbrev = True ,default
parser = argparse.ArgumentParser(prog="tf-stitch",
								description="Starter code with best practices for different Deep Learning problems in one command.",
								epilog="Thanks for Using")

parser.add_argument('output_file',
					type=str,
					help="the output file with starter code"
					)

parser.add_argument('domain',
					type=str,
					help="domain problem type for selecting\
						  appropriate model and dataset"
					)

args = parser.parse_args()

output_extension = os.path.splitext( args.output_file )[-1]

if not (output_extension in ['.py','.ipynb']):
	raise( Exception( " Output File extension must be .py or .ipynb " ) )

content_blocks = stitch_template( args.domain )

with open( args.output_file , "w" ) as file:

	if output_extension==".ipynb":

		notebook_json = stitch_notebook( content_blocks )
		json.dump( notebook_json , file )

	else:

		file.write( "\n\n".join( content_blocks ) )

	file.close()







