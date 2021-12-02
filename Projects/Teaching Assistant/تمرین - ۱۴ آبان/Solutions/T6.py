hight = float(input())
mass = float(input())
bmi = mass / (hight * hight)
print (bmi)
if bmi > 30:
    print ("Fat")
elif bmi > 25:
    print ("Overweight")
elif bmi >18.5:
    print ("Normal")
else:
    print ("Underweight")
