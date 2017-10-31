def Params(oldFunc):
	def inside(*args,**kwargs):
		print("params :",args,kwargs)
		return oldFunc(*args,**kwargs)
	return inside

@Params
def mul(x,y=2):
	print(x*y)

mul(2,3)
mul(2)
mul(x=1,y=3)
