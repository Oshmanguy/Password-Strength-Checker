import re 

#Password strength checker that checks how strong an inputed password is 

passLength = 0
passSpecial = False
passUpper = False
specialPattern = re.compile(r'[^\w\s]') 


userPassword = input("Enter a the password you would like checked: ")

#check diffrent variables of password 

#check if contains uppercase 
passUpper = any(char.isupper() for char in userPassword)
print(passUpper)


#check if contains special characters
if specialPattern.search(userPassword):
    passSpecial = True
else:
    passSpecial = False

print(passSpecial)


#check length 
passLength = len(userPassword)

#Amazing 
if passLength > 13:
    print("Amazing")


#Great 
if passLength > 8:
    print("Great")

#Bad
if passLength < 8:
    print("bad")


