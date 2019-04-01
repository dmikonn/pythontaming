import os

youarehere = os.path.dirname(os.path.realpath(__file__))

with open('output.txt', 'w') as f:
	for root, directories, filenames in os.walk(youarehere):
		for filename in filenames: 
			name, ext = os.path.splitext(filename)
			f.write(ext.lower() + " | " +  filename + " | " +  os.path.join(root,filename) + " |\n") 
