import os

def Exists(oldFun):
	def inside(filename):
		if(os.path.exists(filename)):
			oldFun(filename)
		else:
			print("file not exists")
	return inside

@Exists
def outputLine(infile):
	with open(infile) as f:
		print(f.readlines())

outputLine("test.py")
outputLine('exists.py')
