year=int(input('enter the year'))
if year%4==0:
	if year%100==0:
		if year % 400==0:
			print('leap year')
		else:
			print('is not a leap year')
	else:
		print('its a leap year')
else:
	print('it is not leap year')