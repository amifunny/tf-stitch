import unittest
import os

# Test if a file of correct name is created

class Test(unittest.TestCase):

	# Create folder

	def test_file_exists(self):
		exit_status = os.system( 'tf-stitch out.py -d = {}'.format( 'vision') )
		print( 'tf-stitch out.py -d = {}'.format( 'vision') )
		self.assertEqual( exit_status , 0 )


if __name__=='__main__':
	unittest.main()

# Check file is not empty

# Check for .ipynb and .py

# Check for different option , (right)

# or wrong












