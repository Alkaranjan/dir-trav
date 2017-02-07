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

def main(argv):
	dirName = '';
	try:
		opts, args = getopt.getopt(argv,"hd:",["help=", "dir="])
	except getopt.GetoptError:
		print('usage: trav.py -d <directory name>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			print('usage: trav.py -d <directory name>')
			sys.exit()
		elif opt in ("-d", "--dir"):
			if arg != '':
				path = os.path.dirname(os.path.abspath(__file__)) + "/" + arg
				if os.path.isdir(path):
					dirName = arg
				else:
		 			print('Directory "' + arg + '" does not exists')
		 			sys.exit()


	if dirName == '':
		dirname = 'test'
	path = os.path.dirname(os.path.abspath(__file__)) + "/" + dirName
	trav(path)

if __name__ == "__main__":
   main(sys.argv[1:])

