height = int(input("Enter an even height for the triangle: "))

for h in range (height+1):
    print("*")
    while h!= 0:
        print("" + " " * (h//2 - (h-1)) + "*" *(h+1))