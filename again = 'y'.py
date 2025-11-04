again = 'y'
while again.lower() == 'y':
   diameter = float(input("Enter tube diameter "))
   velocity = float(input("Enter fluid velocity "))
   viscosity = float(input("Enter fluid viscosity "))
   R = (diameter * velocity) / viscosity
   print("Reynolds number =", R)
   if R < 2000:
       print("Laminar flow region")
   elif R > 3000:
       print("Turbulent flow region")
   else:
       print("Transition flow region")
   again = input("Another Reynolds number to calculate? y/n ")