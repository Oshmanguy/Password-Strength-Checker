import customtkinter as ctk
from passStrength import finalPasswordStrengthCheck, weakness, entropyCalc, calcPoolSize, check_pwned_passwords, checkForCommonPass

class PasswordCheckerApp:

    #CONSTRUCTOR 
    def __init__(self, root):

        self.root = root
        self.root.title("Password Strength Checker")

        #Input 
        self.entry = ctk.CTkEntry(self.root, placeholder_text="Enter password")
        self.entry.pack(pady=10)

        #Buttons 
        self.button = ctk.CTkButton(self.root, text="Click Here", command=self.check_password)
        self.button.pack()


        #Output 
        self.result = ctk.CTkLabel(root, text="")
        self.result.pack()


    def check_password(self):
        
        password = self.entry.get()
        entropy = entropyCalc(len(password), calcPoolSize(password))
        password_strength = finalPasswordStrengthCheck(password)
        missing_in_pass = weakness(password)
        known_breaches = check_pwned_passwords(password)
        is_common = checkForCommonPass(password)


        #check if common
        if is_common:
            common_pass_info = "Your password is common"
        else:
            common_pass_info = "Your password is not common"

        #check for known_breaches 
        if known_breaches == 0:
            breach_info = "The password you entered has appeared in no breaches"
        else:
            breach_info = f"The password you entered has appeared in {known_breaches} breaches"



        self.result.configure(
            text=f"Strength: {password_strength}\nEntropy: {entropy:.2f} bits\nMissing: {missing_in_pass}\n{breach_info}\n{common_pass_info}"

        )

    















if __name__ == "__main__":
    root = ctk.CTk()
    app = PasswordCheckerApp(root)
    root.mainloop()