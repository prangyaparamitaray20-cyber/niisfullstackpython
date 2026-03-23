print("A")
try:
	print("try start")
	print(10//0)
	print("end try block")
except ZeroDivisionError:
	print("exception handle")
print("program end")
