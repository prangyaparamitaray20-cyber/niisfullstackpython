a=10
def show():
	a=30
	print(a) #local 30
	print(locals()['a'])#local 30
	print(globals()['a']) #global 10
	globals()['a']=40	
show()
print(a)


