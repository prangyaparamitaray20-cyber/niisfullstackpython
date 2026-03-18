i=1
def show():
	global i
	print("hi")
	i=i+1
	if(i<=3):
		show()
	print("bye")
print("A")
show()
print("B")

