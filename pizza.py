day=input("enter the day..")
pizza=input("enter the pizza.....")
if day=="sunday":
    if pizza=="large":
        print("Browniew")
    elif pizza=="medium":
        print("garlic stick free")
    else:
        print("free coke")
elif day=="monday and tuesday":
    if pizza=="large":
        print("10% discount")
    elif pizza=="medium":
        print("20% discount")
    else:
        print("no discount")
elif  day=="wednesday and thusday":
    if pizza=="every size":
        print("buy 1 get 1 free")
    elif pizza=="large":
        print("coken and garlic stick")
    else:
        print("nothing")
else:
    print("nothing")
