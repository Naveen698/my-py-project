#Multiplication Table 
def calculate():

   num = int(input("Please enter the number: "))

#To display the table
   count = 1
   while count <= 10:
        print(num, ' x ', count, ' = ', num * count)
        count = count + 1
   again()

def again():
    choice = input("Do you want to continue? Please type Y for yes and N for no:")

    if choice.upper() == 'Y':
        calculate()

    elif choice.upper() == 'N':
        print("Bye! See you later")

    else:
        again()

calculate()