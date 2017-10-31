class Player:
	def __init__(self,Id,name,games):
		self.Id = Id
		self.name=name
		self.games=games
	def __str__(self):
		return "my Id is "+str(self.Id)+" name is "+self.name+" and games are "+str(self.games) +" . "
