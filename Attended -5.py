classes=int(input("enter the classes"))
attended = int(input("enter the class attended"))
if attended/classes*100>=75:
	print("it is allowed")
else:
	print("it is not allowed")