s=int(input("enter the s"))
if s<=10000:
	GS=s+(s/100*20)+(s/100*80)
	print(GS)
	if 10000>=s<=20000:
		GS=s+(s/100*25)+(s/100*30)
		print(GS)
		if s>=20000:
		 	GS=s+(s/100*30)+(s/100*95)
		 	print(GS)