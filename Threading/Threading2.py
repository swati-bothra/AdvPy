import threading
import time

class AsyncWrite(threading.Thread):
	def __init__(self,text,filename):
		threading.Thread.__init__(self)
		self.text = text
		self.filename=filename
	def run(self):
		f = open(self.filename,"a")
		f.write(self.text)
		f.close()
		time.sleep(2)
		print("background writing")

def main():
	msg = input("give a msg")
	background = AsyncWrite(msg,"Threading1.txt")
	background.start()
	print("pgm will continue to writing")
	print("10+02")
	background.join()
	print("wait until complete")

if __name__=="__main__":
	main()
