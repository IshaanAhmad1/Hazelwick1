total = 0
hrs = 5
while hrs>0:
    hrs = int(input("Enter hours stayed:"))
    type = input("Is your car electric?")
    if type == "yes":
        total = (hrs*2)
    else:
        total = (hrs*4)
    print("Price is £" total)
print("Price is £0.00")