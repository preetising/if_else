g_date=int(input("enter the g_date..."))
g_month=int(input("enter the g_month..."))
g_year=int(input("enter the g_year..."))
r_date=int(input("enter the r_date.."))
r_month=int(input("enter the r_month.."))
r_year=int(input("enter r_year..."))
if g_year==r_year:
    if g_month==r_month:
        if g_date==r_date:
            print("no fine")
        else:
            print("your fine 15*(g_date-r_date")
    else:
        print(500*(g_month-r_month))
else:
    print(10,000)

