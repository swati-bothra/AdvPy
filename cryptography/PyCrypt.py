import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key,filename):
	outputfile = "encrypted" + filename
	chunksize = 64*1024
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)
	encryptor = AES.new(key,AES.MODE_CBC,IV)

	with open(filename,'rb') as infile:
		with open(outputfile,'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)
			while True:
				chunk = infile.read(chunksize)
				if len(chunk)==0:
					break
				elif len(chunk)%16 !=0:
					chunk += b' ' * (16-(len(chunk)%16))
				outfile.write(encryptor.encrypt(chunk))

def decrypt(key,filename):
	chunksize = 64*1024
	outputfile = filename[9:]
	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key,AES.MODE_CBC,IV)
		with open(outputfile,'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				if(len(chunk)==0):
					break
				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def getKey(pswd):
	hasher = SHA256.new(pswd.encode('utf-8'))
	return hasher.digest()


def main():
	choice = input("want to Encrypt(E) OR Decrypt(D) ?")
	if choice == 'E':
		filename=input("give your filename to encrypt :")
		pswd= input("give key to encrypt :")
		encrypt(getKey(pswd),filename)
		print("Done!")
	elif choice == 'D':
		filename = input("file to decrypt :")
		pswd = input("key to decrypt :")
		decrypt(getKey(pswd),filename)
		print("Done!")
	else:
		print("no option is selected!")

if __name__=='__main__':
	main()








