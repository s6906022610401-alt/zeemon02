num_employees = int(input("Enter number of mployees : "))
if num_employees < 50:
    print("this is a small company.")
elif num_employees < 250:
    print("this is a medium-sized company.")
elif num_employees >= 250:
    print("this is a large company.")