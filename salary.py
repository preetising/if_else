salary=int(input("enter the salary"))
year=int(input("enter year of service"))
if year>=5:
	print('bouns is 5 % = ', 5*salary/100+salary)
else:
	print("no bonus")