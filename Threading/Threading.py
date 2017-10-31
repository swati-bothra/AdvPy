import threading
import time

lock = threading.Lock()

def Timer(name,delay,repeat):
	print("thread started : "+ name)
	lock.acquire()
	print("lock aquired")
	while repeat>0:
		repeat -=1
		time.sleep(delay)
		print(name + " : time is " + str(time.ctime(time.time())))
	print(name + " :  completed")
	print("lock released")
	lock.release()

def main():
	t1 = threading.Thread(target=Timer, args=("t1",1,5))
	t2 = threading.Thread(target=Timer, args=("t2",1,5))
	t1.start()
	t2.start()
	print("main completed")

if __name__=="__main__":
	main()
