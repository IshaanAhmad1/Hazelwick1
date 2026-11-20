ans1 = float(input("Given that y = 2x² + 3x + 1, enter the sum of the value of the x values of the stationary point and roots: "))
ans2 = float(input("Enter the value of 8 minus 3: "))
ans3 = float(input("Enter the product of coefficient of the derivatives of 5x² - 2x + 3 and x² - x - 5: "))
ans4 = float(input("Enter the value of 5 divided by 5: "))
score = 0
if ans1 == -2.25:
    score = score + 1
else:
    pass
if ans2 == 5.0:
    score = score + 1
else:
    pass
if ans3 == 9.0:
    score = score + 1
else:
    pass
if ans4 == 1.0:
    score = score + 1
else:
    pass
print(f"Your final score is {score} out of 4.")