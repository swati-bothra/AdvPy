import socket

def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host,port))
	print("server started")
	while True:
		data, add = s.recvfrom(1024)
		data = data.decode('utf-8')
		print("msg from client " + data)
		data = data.upper()
		print("data send to client "+ data)
		s.sendto(data.encode('utf-8'),add)
	s.close()
if __name__=='__main__':
	main()
