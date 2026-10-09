import random
ans1 = (random.randint(1,100))
while True:
    computer_ans = (random.randint(1,100))
    for i in range(10):
        user_ans = int(input("Enter a number 1-100: "))
        if computer_ans < user_ans:
            print("Your answer is too high.")
        if computer_ans > user_ans:
            print("Your answer is too low.")
        if computer_ans == user_ans:
            exit("You win!")
    print("You lose!")