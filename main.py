import argparse

# if __name__=='__main__':
	
print("init m")

# Important features 
# reqired = bool , True default 
# allow_abbrev = True ,default
# 
parser = argparse.ArgumentParser(prog="sq",
								description="It's a SOTA Squareer",
								epilog="You have been tricked")
parser.add_argument('-an',
					'--add_number',
					metavar='add_number',
					default=2,	
					type=float,
					help="the number to add"
					)

args = parser.parse_args()

print("Square of number is {}".format(args.add_number**2))

