import random
num6 = 0
for i in range (20):
    num1 = random.randint(1,5)
    num2 = random.randint(0,1000)
    num4 = random.randint(0,1000)
    if num1 == 1:
            num5 = num2 + num4
            guess = int(input("Enter the answer:"))
            if guess == num5:
                num6 = num6 + 1
    elif num1 == 2:

    elif num1 == 3:

    elif num1 == 4:

    elif num1 == 5:

