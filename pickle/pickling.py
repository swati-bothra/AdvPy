import pickle
from Player import Player

games=['s','w','v']

myObj = Player(1,"swati",games)
print(myObj)

with open('dumpfile.pkl','wb') as outfile:
	pickle.dump(myObj,outfile,pickle.HIGHEST_PROTOCOL)

print("********************************")

newObj=None
with open('dumpfile.pkl','rb')as infile:
	newObj = pickle.load(infile)

print(newObj)
