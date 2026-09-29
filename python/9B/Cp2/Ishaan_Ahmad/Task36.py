import random
computer_ans = (random.randint(1,100))
user_ans = int(input("Enter a number 1-100: "))
for i in range(10):
    if computer_ans > user_ans:
        print("Your answer is too high.")
    else:
        print("Your answer is too low.")