side1=int(input( "enter the side 1"))
side2=int(input("enter the side 2"))
side3 =int (input("enter the side3"))
if side1==side2==side3:
	print(" it is equilateral triangle")
elif side1==side2 !=side3 or side2 == side3 !=side1 or side3==side1!=side2:
	print (" isosceles triangle")
else:
	print(" scalene triangle")