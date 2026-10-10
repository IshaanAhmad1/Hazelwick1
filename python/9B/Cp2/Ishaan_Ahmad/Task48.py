height = int(input("Enter an even height for the triangle: "))
for h in range (0,(height+1)):
      for i in range (1):
       if h%2==1:
          print(" "*(height+1-h) + "* "*h)
       else:
          print(" "*(height-h) + " *"*h)