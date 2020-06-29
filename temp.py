import json

with open('template.json',"rb") as file:
	content = json.loads( file.read() )
	file.close()

print( content['domain'].vision.model )
