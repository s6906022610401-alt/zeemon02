#Program to compare the strings "Hary" and "Hark"
#Define the strings
string1 = "Mary"
string2 = "Mark"
#Compare the strings for equality
if string1 == string2 :
    print(f'"{string1}"and "{string2}" are equal.')
else:
    print(f'"{string1}"and "{string2}" are not equal.')
#Lexicographical comparison
if string1 < string2:
    print(f'"{string1}" comes before "{string2}" inlexicographical order.')
elif string1 > string2:
    print(f'"{string1}" comes after "{string2}" in lexicographical order. ')
#Case-insensitive comparison
if string1.lower() == string2.lower():
    print(f'"{string1} and {string2} are equal when case is gnored.')
else:
    print(f'"{string1}" and "{2}" are not equal when case is gnored.') 