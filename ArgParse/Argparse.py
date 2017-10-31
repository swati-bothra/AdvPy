import argparse

def fibb(n):
	a, b = 0, 1
	for i in range(n):
		a, b =  b, a+b
	return a

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num",type=int,help="fibboo at position u want")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v","--verbose",action="store_true")
	group.add_argument("-q","--quiet",action="store_true")
	parser.add_argument("-o","--output",help="outputting the ans in file",action = "store_true")
	args = parser.parse_args()
	result = fibb(args.num)
	if args.output:
		f = open("fibb.txt","a")
		f.write(str(result)+ "\n")
		f.close
	if args.verbose:
		print "the fibb no. of " + str(args.num)+ " is " + str(result)
	elif args.quiet:
		print str(result)
	else:
		print "the ans is "+ str(result)
	
if __name__ == "__main__":
	main()

