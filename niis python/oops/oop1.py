class Demo:
	#classmethod  it call by classname  but  it call  by object
	@classmethod
	def show(cls):
		print("hi")
Demo.show() #it call by classname  better
d=Demo()
d.show() # it call by object



















