import random
num6 = 0
for i in range (20):
    num1 = random.randint(1,5)
    num2 = random.randint(0,1000)
    num4 = random.randint(0,1000)
    if num1 == 1:
        num5 = num2 + num4
        guess = int(input(f"Enter the answer of {num4} added to {num2}:"))
        if guess == num5:
            num6 = num6 + 1
    elif num1 == 2:
        num5 = num2 - num4
        guess = int(input(f"Enter the answer of {num2} subtracted by {num4}:"))
        if guess == num5:
            num6 = num6 + 1

    elif num1 == 3:
        num5 = num2 * num4
        guess = int(input(f"Enter the answer of {num4} multiplied by {num2}:"))
        if guess == num5:
            num6 = num6 + 1

    elif num1 == 4:
        num5 = num2 // num4
        guess = int(input(f"Enter the answer of {num2} divided by {num4}:"))
        if guess == num5:
            num6 = num6 + 1

    elif num1 == 5:
        num5 = num2 ** num4
        guess = int(input(f"Enter the answer of {num2} to the power of {num4}:"))
        if guess == num5:
            num6 = num6 + 1

print("You got ", num6, " points out of 20!")