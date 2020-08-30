#A Simple Calculator
# This is for operations
def calculate():
    operation = input('''Please choose any one of the operations :
        1 for addition
        2 for subtraction
        3 for multiplication
        4 for division
        5 for percentage to number
        6 for finding percentage
        7 for square root
        8 for square
         :''')

    if operation ==  '1':
        num1 = float(input(" Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))

        print('{} + {} ='.format(num1, num2))
        print(num1 + num2)

    elif operation == '2':
        num1 = float(input(" Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))

        print('{} - {} ='.format(num1, num2))
        print(num1 - num2)

    elif operation == '3':
        num1 = float(input(" Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))

        print('{} x {} ='.format(num1,num2))
        print(num1 * num2)

    elif operation == '4':
        num1 = float(input(" Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))

        print('{} ÷ {} ='.format(num1,num2))
        print(num1 / num2)

    elif operation == '5':
        num1 = float(input(" Please enter the number:"))

        print('{} % ='.format(num1))
        print(num1 / 100)

    elif operation == '6':
        num1 = float(input("Please enter the number:"))

        print('{} ='.format(num1))
        print(num1 * 100)

    elif operation == '7':
        num1 = float(input("Please enter the number:"))

        print('Square root of {} ='.format(num1))
        print(num1 ** 0.5)

    elif operation == '8':
        num1 = float(input("Please enter the number:"))

        print('Square of {} ='.format(num1))
        print(num1 ** 2)

    else:
         print("Sorry, please type again!")

#This is for repeating the process
    again()
def again():
     calc_again = input("Do you want to continue? Please type Y for yes and N for no:")

     if calc_again.upper() == 'Y':
       calculate()

     elif calc_again.upper() == 'N':
       print("Thanks for calculating here. See you later! Bye!")

     else:
        again()


calculate()

