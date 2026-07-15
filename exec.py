howoeked = int(input ("Enter the number of hours worked: "))
rate = int(input ("Enter hourly pay rate: "))

if howoeked <= 40:
    gp = howoeked * rate
else:
    ovt = howoeked > 40
    gp = (40 * rate)+(ovt*rate*1.5)
print(f"The gross pay is ${gp:.2f}")
