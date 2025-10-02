import customtkinter as ctk
from passStrength import finalPasswordStrengthCheck, weakness, entropyCalc, calcPoolSize

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

        self.result.configure(
            text=f"Strength: {password_strength}\nEntropy: {entropy:.2f} bits\nMissing: {missing_in_pass}"

        )















if __name__ == "__main__":
    root = ctk.CTk()
    app = PasswordCheckerApp(root)
    root.mainloop()