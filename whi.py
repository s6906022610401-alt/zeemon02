import random
print ("What is my magic number (1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and "____________________ ":
    msg = str(ntries) + ">>"
    if (ntries == 6):
        "______________________"
    yourguess = int(input(msg))
    if  " _________________" :
        print("--> too high")
        
    if "______________________" :
        print("--> too low")
        ntries += 1
    
    if "______________________" :
        print("yes! it's",mynumber)
else :
    print("soory my number is ",mynumber)