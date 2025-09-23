import re 

#check diffrent variables of password 

#check if contains uppercase 
def contianUpper(password):
    return any(char.isupper() for char in password)


#check if contains special characters

def containSpecial(password):

    specialPattern = re.compile(r'[^\w\s]')  

    if specialPattern.search(password):
        return True
    else:
        return False



#check length 
def checkLength(password):
    passLength = len(password)

    #Amazing 
    if passLength > 13:
        return 2


    #Great 
    if passLength > 8:
        return 1

    #Bad
    if passLength < 8:
        return 0



#Give user final review on password 
def finalPasswordStrengthCheck(password):

    #calculate final strength based on integer score 
    finalPasswordScore = 0
    
    if contianUpper(password):
        finalPasswordScore = finalPasswordScore + 1

    if containSpecial(password):
        finalPasswordScore = finalPasswordScore + 1

    finalPasswordScore += checkLength(password)

    
    if finalPasswordScore >= 4:
        return "Strong"
    elif finalPasswordScore == 2:
        return "Moderate"
    elif finalPasswordScore <= 1:
        return "Weak"

#--------------------MAIN------------------------------------------------------------

userPassword = input("Enter a the password you would like checked: ")
print(finalPasswordStrengthCheck(userPassword))
