height = int(input("Enter the height of the triangle: "))
for h in range (0,(height+1)):
      if h%2==1:
         print(" "*(height+1-h) + "* "*h)
      else:
         print(" "*(height-h) + " *"*h)