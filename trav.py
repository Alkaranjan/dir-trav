import os, sys, getopt

def printContents(filePath):
	print("reading file contents from - " + filePath)
	with open(filePath, 'r') as fin:
		print(fin.read(), end="")
	print("\ndone..\n")

def trav(dirPath):
	for root, dirs, files in os.walk(dirPath):
		print("working in directory - " + root)
		for file in files:
			printContents(root + "/" + file)

def printOptions():
	msg = """usage: trav.py [options]

Options:
	-h, --help       This help menu.
	-d <directory>, --directory=<directory>    Give a directory name to work in.
"""
	print(msg)

def main(argv):
	dirName = '';
	try:
		opts, args = getopt.getopt(argv,"hd:",["help", "directory="])
	except getopt.GetoptError:
		printOptions()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			printOptions()
			sys.exit()
		elif opt in ("-d", "--directory"):
			if arg != '':
				path = os.path.dirname(os.path.abspath(__file__)) + "/" + arg
				if os.path.isdir(path):
					dirName = arg
				else:
		 			print('Directory "' + arg + '" does not exists')
		 			sys.exit()
			else:
				printOptions()
				sys.exit(2)


	if dirName == '':
		dirName = 'test'
	path = os.path.dirname(os.path.abspath(__file__)) + "/" + dirName
	if os.path.isdir(path):
		trav(path)
	else:
		print('default directory "test" not found')
		sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])

