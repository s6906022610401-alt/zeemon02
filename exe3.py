howoeked = int(input ("Enter the number of hours worked: "))
rate = int(input ("Enter hourly pay rate: "))

if howoeked <= 50:
    gp = howoeked * rate
else:
    ovt = howoeked > 50
    gp = (50 * rate)+(ovt*rate*1.5)
    gp = rate + ovt
print(f"The gross pay is $" ,gp)
