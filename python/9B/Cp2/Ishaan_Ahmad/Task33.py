score = 0
for i in range (0,5):
    num1 = int(input("Give an integer 1 to 100: "))
    import random
    ans1 = (random.randint(1,100))
    
    if num1 == ans1:
        print("bang-on (correct)")
        score = score + 10
    else:
        if ans1-5 <= num1 <= ans1+5:
            print("close (within 5)")
            score = score + 5
        else:
            if ans1-10 <= num1 <= ans1+10:
                print("okay (within 10)")
                score = score + 2
            else:
                print("way off")
print("Your final score is: ", score)