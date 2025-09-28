import re 
import math as m
import hashlib 
import requests



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

#fix load list of common passwords and store them into a list 
def load_wordlist():
    common_passwords = []
    with open("wordlists/10k-most-common.txt", "r", encoding="utf-8") as file:
        common_passwords = [line.strip() for line in file]
    return common_passwords


#print(load_wordlist())#TESTING GET RID OF LATER 

#This function will check the common password list to see if it matches any of the common passwords 
def checkForCommonPass(userPassword):

    wordlist = load_wordlist()#create wordlist to hold all passwords


    if userPassword in wordlist: #lookup of O(1) instead of for loop 
        print("IS ON LIST")
        return True
    else:
        print("IS NOT ON LIST")
        return False
    

#Function that makes a hash out of the user given password using the SHA-1 algorithm 
def hashPassword(userPassword):

    sha1_hasher = hashlib.sha1() #create "hasher" for the sha1 algorithm 

    encoded_string = userPassword.encode('utf-8') #encode stringt to bytes using UTF-8

    sha1_hasher.update(encoded_string) #give hashing algorithm the string/password

    hashedPass = sha1_hasher.hexdigest() #convert from bytes to hexadecimal string 

    return hashedPass

#returns the first 5 characters in the string of the hashed password 
def fiveCharsOfHash(hashedPassword):

    full_hash = hashedPassword

    return full_hash[0:5]














#Give user final review on password 
def finalPasswordStrengthCheck(password):

    #check if password matches the list of common passwords before anything 
    if checkForCommonPass(password):
        return "Weak"


    if entropy <= 28:
        return "Weak"
    elif 29 <= entropy <= 59:
        return "Moderate"
    else:
        return "Strong"
    
    
def weakness(password):

    missingStrengths = [] #empty list, append values as see fits 


    if contianUpper(password) == False:
        missingStrengths.append("Uppercase")
    if containLower(password) == False:
        missingStrengths.append("Lowercase")
    if containNumbers(password) == False:
        missingStrengths.append("Numbers")
    if containSpecial(password) == False:
        missingStrengths.append("Special Characters")

    return missingStrengths




#--------------------MAIN------------------------------------------------------------

userPassword = input("Enter a the password you would like checked: ")

#assign entropy to a variable 
entropy = entropyCalc(len(userPassword), calcPoolSize(userPassword))

print("")
print("---------------------------------------------------")
print("Password Strength: " + str(finalPasswordStrengthCheck(userPassword)))
print("Missing: "+ str(weakness(userPassword)))
print(f"Estimated Entropy: {entropy:.2f} bits")
print(checkForCommonPass(userPassword))
print("---------------------------------------------------")
print(hashPassword(userPassword))
print(fiveCharsOfHash(hashPassword(userPassword)))
print("")

