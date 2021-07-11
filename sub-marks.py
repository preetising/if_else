physics=int(input('enter your marks in physics'))
chemistry=int(input('enter your marks in chemistry'))
biology=int(input('enter your marks in biology'))
mathemetics=int(input('enter your marks im mathemetics'))
computer=int(input('enter your marks in computer'))
sum=physics+chemistry+biology+mathemetics+computer
pre=sum/500*100
print(sum)
print(pre) 
if pre>=90:
	print('Grade A')
elif pre>=80:
	print('Grade B')
elif pre>=70:
    print('Grade C')
elif pre>=60:
	print('Grade D')
elif pre>=40:
    print('Grade E')
else:
 	('nothing')