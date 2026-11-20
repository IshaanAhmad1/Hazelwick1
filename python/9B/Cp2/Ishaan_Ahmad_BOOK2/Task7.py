shop = ["milk", "bread", "baked beans", "bananas", "butter", "battleships"]
want = input("Enter your item: ")

num = 0
for i in range (0,5):
    if shop[i] == want:
        print("Your item is on the list in number", (i+1))
        num = num + 1
if num == 0:
    print("Your item is not on the list.")