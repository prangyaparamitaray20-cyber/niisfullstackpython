print("A")
try:
	print("try start")
    print(10//0)
	print("end try block")
except IndexError:
	print("exception handle")
print("program end")
