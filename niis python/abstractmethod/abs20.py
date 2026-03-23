
class NegativeError(BaseException):
	def _init_(self):
		print("negative number not allow")
print("enter a number ")
no=int(input())
if no<0:
	try:
		raise NegativeError()
	except:
		print("exception caught negative number not allow ")
else:
	print("number=",no)
print("program end")

