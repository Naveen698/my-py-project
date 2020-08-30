# AN INTREST CALCULATOR
def si():
   P = float(input("Please enter the principle in ₹: "))

   T = float(input("Please enter the time in years: "))

   R = float(input("Please enter the rate of intrest: "))

   result = P * T * R / 100

   print("The intrest is ₹", result)

   again() 

def ci(): 

   P = float(input("Please enter the principle in ₹: "))

   T = float(input("Please enter the time in years: "))

   R = float(input("Please enter the rate of interest: "))

   result = P * (pow((1 + R / 100), T))

   print("The amount is ₹", result)

   CI = result - P

   print("The intrest is ₹", CI) 

   again() 

def calculate():
    print("WELCOME TO THIS INTREST CALCULATOR🙏🏻🙏🏻🙏🏻!") 
    intrest = input('''Please choose which type of intrest to calculate:
        1 for simple intrest
        2 for compound interest 
        :''')
    
    if intrest == '1':
        si() 
        
    elif intrest == '2':
        ci() 
        
    else:
        print("Please enter the correct value again") 
        calculate() 
        
def again():
    
    opinion = input("Do you want to continue? Please type Y for yes and N for no: ") 
    
    if opinion == 'Y':
        calculate()
        
    elif opinion == 'N':
        print("Bye! See you later👋🏻👋🏻🤗🤗!") 
        
    else:
        again()
        
calculate() 
