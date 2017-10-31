import re
import argparse

def main():
	parser =  argparse.ArgumentParser()
	parser.add_argument("pattern",help="pattern u want to find in string")
	parser.add_argument("ffile",help="file in you wan to search")
	args = parser.parse_args()
	f= open(args.ffile)
	lineNum = 0
	for line in f.readlines():
		line= line.strip('\n\r')
		lineNum += 1
		ans1 = re.search(args.pattern,line,re.M|re.I)
		if ans1:
			print (str(lineNum)+ " : " +line)

if __name__ == "__main__":
	main()

