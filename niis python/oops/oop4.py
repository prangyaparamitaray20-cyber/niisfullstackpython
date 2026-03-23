class Demo:
	def show(self):
		print("instance show method")
	@classmethod
	def look(cls):
		print("class look method")
	@staticmethod
	def disp():
		print("disp static method")
d=Demo()
Demo().show() # by object call
d.show()  # it call by object  refernce 
d.look()
d.disp()
#Demo.show()  error
Demo.look()
Demo.disp()

