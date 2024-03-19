# Create a Class 
class Calculator:

    def __init__(self,num1, num2, sign) -> None:
        self.num1 = num1
        self.num2 = num2
        self.sign = sign

    def addition(self):
        if (self.sign == "+"):
            addition = self.num1 + self.num2
            print("Addition is:" , addition)
        else:  
            return "   "    
    def subtraction(self):
        if (self.sign == "-"):
            subtraction = self.num1 - self.num2
            print("Subtraction is: ", subtraction)
        else:
            return "  "

    def multiplication(self):
        if (self.sign == "*"):
            multiplication = self.num1 * self.num2
            print("Multiplication is: ", multiplication)
        else:
            return "  "
        
    def modulo(self):
        if (self.sign == "%"):
            modulo = self.num1 % self.num2
            print("Modulos is: ", modulo)
        else: 
            return "  "
        
    def division(self):
        if (self.sign == "/"):
            division = self.num1 / self.num2
            print("Division is: " , division)
        else:
            return "  "




print("Pick a sign to get the basic operation: ")
print("Addition "+ "+  ")
print("Subtraction "+ "- ")
print("Division " + "/ ") 
print("Modulo " +  "% ")
print("Multiplication "+ "* ")
first_user = Calculator(sign =str(input("Enter SIGN here: ")) ,    
num1 = int(input("Enter the first number: ")),
num2 = int(input("Enter the second number: ")))
addition = first_user.addition()


subtraction = first_user.subtraction()

division = first_user.division()

modulo = first_user.modulo()

multiplication = first_user.multiplication()


