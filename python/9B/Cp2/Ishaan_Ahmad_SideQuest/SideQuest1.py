n = int(input("Select a line from pascal's triangle e.g 1: "))

def pascal(n):
    a = [1]
    for i in range(n):
        a.append(1)
   while len(a)<=n:
    
   
   
   
   
   
   
   
   
    for i in range(1, n//2):
        a[i] = a[i+1] + a[i-1]
        a[(n-i)] = a[i]
    print(a)

pascal(n)