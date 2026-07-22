input_s = input("enter a string: ")
modified_s = " "
vowels = "aeiouAEIOU"

for char in input_s:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_s += "*"
    else:
        modified_s += upper_char
print("modified string:",modified_s)