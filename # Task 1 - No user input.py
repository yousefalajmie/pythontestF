diameter = 0.1
velocity = 12
viscosity = 0.00015
R = (diameter * velocity) / viscosity
print("Reynolds number =", R)
if R < 2000:
   print("Laminar flow region")
elif R > 3000:
   print("Turbulent flow region")
else:
   print("Transition flow region")

diameter = 1.5
velocity = 0.1
viscosity = 0.0002
R = (diameter * velocity) / viscosity
print("\nReynolds number =", R)
if R < 2000:
   print("Laminar flow region")
elif R > 3000:
   print("Turbulent flow region")
else:
   print("Transition flow region")