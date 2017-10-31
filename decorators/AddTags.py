def AddTags(*tags):
	def decorator(oldFunc):
		def inside(*args,**kwargs):
			code = oldFunc(*args,**kwargs)
			for tag in reversed(tags):
				code = "<{0}>{1}</{0}>".format(tag,code)
			return code
		return inside
	return decorator

@AddTags("p","b","i")
def main(name):
	return "my name is "+ name 

print(main('Swati Bothra'))
