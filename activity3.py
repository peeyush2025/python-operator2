height=float(input("enter your height in cm :"))
weight=float(input("enter your weight in kg :"))
bmi=weight/(height/100)**2
print("your bmi is ",bmi)
if bmi <=18.4 :
    print("your are underweight.")
elif bmi <=24.9:
    print("your healthy.")
elif bmi <= 29.9:
    print("your over weight.")
elif bmi <= 34.9:
    print("you are severly over weight.")
elif bmi <= 39.9:
    print("your obese.")
else:
    print("your severly obese.") 