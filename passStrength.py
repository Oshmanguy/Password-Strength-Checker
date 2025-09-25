import re 
import math as m



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
    
#Entropy Calculation 
def entropyCalc(lengthOfPass, poolSize):

    #calculate entropy 
    return m.log2((poolSize ** lengthOfPass))

    
#function that calculats pool size for entrophy calculation 
def calcPoolSize(password):

    #Start pool size at zero
    poolSize = 0

    if contianUpper(password):
        poolSize = poolSize + 26 #add 26 to pool since thats how many letters are in alphabet 
    if containLower(password):
        poolSize = poolSize + 26 #same reason, 26 upper case letters 
    if containSpecial(password):
        poolSize = poolSize + 32 #there are 32 special characters on the average keyboard 
    if containNumbers(password):
        poolSize = poolSize + 10 #there are 10 numbers to choose from on the keyboard 

    return poolSize 


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

    if finalPasswordScore >= 6:
        return "Strong"
    elif finalPasswordScore == 4 :
        return "Moderate"
    elif finalPasswordScore <= 3:
        return "Weak"
    else:
        return "Moderate"#fix later  
    


def weakness(password):
    if contianUpper(password) == False:
        print("Missing Uppercase")
    if containLower(password) == False:
        print("Missing lowercase")
    if containNumbers(password) == False:
        print("Missing Numbers")
    if containSpecial(password) == False:
        print("Missing Special Characters")

#--------------------MAIN------------------------------------------------------------

userPassword = input("Enter a the password you would like checked: ")

#assign entropy to a variable 
entropy = entropyCalc(len(userPassword), calcPoolSize(userPassword))

print("Password Strength: " + str(finalPasswordStrengthCheck(userPassword)))
print("Reason: ")
weakness(userPassword)
print(f"Estimated Entropy: {entropy:.2f} bits")

