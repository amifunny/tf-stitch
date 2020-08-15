# Subprocess to run CLI for package
import subprocess
import unittest
import os

MODULE = "python -m tf_stitch"
MODULE_ARG = MODULE.split()
# File to generate
FILENAME = "output.py"

class Test(unittest.TestCase):

	def execute_query( self, args, filename=FILENAME ):

		"""
			Execute command to generate stitched file
			with given arguments

			return - A subprocess.CompletedProcess Object
		"""

		if len(args)==0:
			subprocess_arg = MODULE_ARG + [ filename ]
		else:	
			subprocess_arg = MODULE_ARG + [ filename, *args ]

		output = subprocess.run(
            		subprocess_arg	
        		)

		return output

	def checkpoint( self, process_result ):

		"""
			Return (boolean) : If there was no error and 
			generated a non-empty file, return True.
			else False.
			Also remove the generated file.
		"""

		# check if status code was not 0;
		# i.e. If a error occured
		if process_result.returncode!=0:
			return False

		# Fourth argument is always filename
		generated_file = process_result.args[3]
		# Check if a file with given filename was generated
		is_exists = os.path.exists( generated_file )

		if is_exists:
			
			# If generated, check if it is empty
			is_empty = os.path.getsize( generated_file ) == 0
		
			# cleanup the generated file
			os.remove( generated_file )
			
			if not is_empty:
				return True

		return False	


	def test_py_simple(self):
		"""
			Check for `domain` argument only.
		"""
		test_args = [
			"-d=vision"
		]

		query_result = self.execute_query( test_args )
		self.assertTrue( self.checkpoint(query_result) )


	def test_ipynb_simple(self):

		"""
			Check notebook genration with `domain` argument only.
		"""

		test_args = [
			"-d=nlp"
		]

		notebook_file = FILENAME.split(".")[0] + ".ipynb"

		query_result = self.execute_query( test_args , notebook_file )
		self.assertTrue( self.checkpoint(query_result) )

	def test_py_all_args(self):

		"""
			Check for extensive list of arguments with
			dataset and	model arguments
		"""

		test_args = [
			"--dataset=cifar100",
			"--model=conv",
			"--training=custom",
			"--testing=True"
		]

		query_result = self.execute_query( test_args )
		self.assertTrue( self.checkpoint(query_result) )

	def test_py_wrong_args(self):

		"""
			Check if error occurs for wrong argument
		"""

		test_args = [
			"--dataset=cifar100",
			"--model=wrong_model",
			"--training=custom",
			"--testing=True"
		]

		query_result = self.execute_query( test_args )
		self.assertFalse( self.checkpoint(query_result) )

	def test_py_no_args(self):

		"""
			Check if error occurs for no arguments
		"""

		test_args = []

		query_result = self.execute_query( test_args )
		self.assertFalse( self.checkpoint(query_result) )


if __name__=='__main__':
	unittest.main()












