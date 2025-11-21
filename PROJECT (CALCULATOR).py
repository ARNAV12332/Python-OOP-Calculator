class Calculator:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        soln = self.value1 + self.value2
        print("Result:", soln)
        return soln
    
    def subtraction(self):
        soln = self.value1 - self.value2
        print("Result:", soln)
        return soln
    
    def divide(self):
        if self.value2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        soln = self.value1 / self.value2
        print("Result:", soln)
        return soln

    def multi(self):
        soln = self.value1 * self.value2
        print("Result:", soln)
        return soln


if __name__ == "__main__":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    calc = Calculator(a, b)

    print("\n\t\t\tWELCOME TO CALC v.1")
    print("\t\t\tSelect An Operation")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")

    choice = int(input("\nEnter Your Choice (1,2,3,4): "))

    if choice == 1:
        calc.add()   # added parentheses
    elif choice == 2:
        calc.subtraction()
    elif choice == 3:
        calc.divide()
    elif choice == 4:
        calc.multi()
    else:
        print("We cannot find the request. Please try again.")
