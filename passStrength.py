import re 

#check diffrent variables of password 

#check if contains uppercase 
def contianUpper(password):
    return any(char.isupper() for char in password)

#check if contains lower
def containLower(password):
    return any(char.islower() for char in password)


#check if contains special characters
def containSpecial(password):

    specialPattern = re.compile(r'[^\w\s]')  

    if specialPattern.search(password):
        return True
    else:
        return False
    

#check if contains numbers 
def containNumbers(password):
    return any(char.isdigit() for char in password)



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
    
    #Count up score for containing lowercase chars
    if containLower(password):
        finalPasswordScore = finalPasswordScore + 1

    #Count up score for containing uppercase chars
    if contianUpper(password):
        finalPasswordScore = finalPasswordScore + 1

    #Count up score for containing special chars
    if containSpecial(password):
        finalPasswordScore = finalPasswordScore + 1

    #Count up score for containing
    if containNumbers(password):
        finalPasswordScore = finalPasswordScore + 1

    finalPasswordScore += checkLength(password)

    print(finalPasswordScore)

    if finalPasswordScore >= 6:
        return "Strong"
    elif finalPasswordScore == 4 :
        return "Moderate"
    elif finalPasswordScore <= 3:
        return "Weak"


#--------------------MAIN------------------------------------------------------------

userPassword = input("Enter a the password you would like checked: ")
print(finalPasswordStrengthCheck(userPassword))
