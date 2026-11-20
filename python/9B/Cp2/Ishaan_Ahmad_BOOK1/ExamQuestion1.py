price = 0
for i in range (8):
    height = int(input("Enter your height in cm: "))
    if height>=140:
        print("You can ride alone.")
        print("You must pay £22.49")
    elif 120<=height<140:
        check = input("Are you with an adult?")
        if check == "yes":
            print("You can go with an adult.")
            print("You must pay £31.48.")
            i = i+1
        else:
            print("You cannot go on the ride.")
            i = i-1
    else:
        print("You cannot go on the ride.")
        i = i-1