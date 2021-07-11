print("welcome")
print("swip your card")
pin=int(input("enter your pin"))
amt=int(input("enter your amt"))
if pin ==pin:
	trans = input('Balance enquiry, withdrawl,diposit,quit..')
	if trans=="Balance enquiry" :
		print(amt)
	elif trans=="withdrawl":
		a=int(input("enter the your amount"))
		amt=amt-a
		print('take your cash')	
		print('reminering your ammount',amt)
	elif trans=="diposit":
		b=int(input("enter the amount"))
		amt=amt+b
		print("your total amount=",amt)
	elif trans=="quit":
			print("exit")
else:
	print("pin is wrong")