from string import Template

class MyTemp(Template):
	delimiter = '#'

def main():
	cart = []
	cart.append(dict(a='swati',b='jain'))
	cart.append(dict(a='kar',b='bot'))
	cart.append(dict(a='kj',b='sk'))
	t = MyTemp('#a #b')
	for name in cart:
		print t.substitute(name)

if __name__=='__main__':
	main()


