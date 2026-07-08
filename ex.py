weight = float(input("enter your weight in kg"))
hight = float(input("enter your hight in m"))
print ("your hight is {hight} m.")
print ("your weight is {weight} kg.")

Bmi = weight/ (hight /10 ** 2)
print("your bmi is",format(Bmi, ".2f"))