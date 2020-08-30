# Area calculator
#Input from user 
def calculate():
    print("WELCOME TO THIS AREA CALCULATOR!") 
    choice = input('''Please choose the figure's area that you want to calculate:
        1 for triangle
        2 for square
        3 for rectangle
        4 for rhombus
        5 for trapezium
        6 for general quadrilateral
        7 for parallelogram
        8 for circle
        : ''') 

    if choice == '1':
        triangle()

    elif choice == '2':
        square()

    elif choice == '3':
        rectangle()

    elif choice == '4':
        rhombus()

    elif choice == '5':
        trapezium()

    elif choice == '6':
        GQ()

    elif choice == '7':
        parallelogram()

    elif choice == '8':
        circle()

    else:
        print("Invalid Input")

#Calculation of Triangle
def triangle():
    a = float(input("Please enter the first side: ")) 
    b = float(input("Please enter the second side: ")) 
    c = float(input("Please enter the third side: ")) 

    s = (a + b + c) / 2

    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print('The area of the triangle is', area,'sq.units')

    again()

#Calculation for square
def square():
    side = float(input("Please enter the side of the square: ")) 
    
    area = side ** 2
    
    print('The area of the square is', area,'sq.units')
   
    again()
#Calculation for rectangle
def rectangle():
    length = float(input("Please enter the length of the rectangle: "))
    breadth = float(input("Please enter the breadth of the rectangle: "))

    area = length * breadth
   
    print('The area of the rectangle is', area, 'sq.units')
   
    again()
 #Calculation of rhombus
def rhombus():
    d1 = float(input("Please enter the first diagonal: "))
    d2 = float(input("Please enter the second diagonal: "))

    area = 1/2 * d1 * d2
   
    print('The area of the rhombus is', area, 'sq.units')
   
    again()
#Calculation for trapezium 
def trapezium():
    h = float(input("Please enter the height of the trapezium: "))
    a = float(input("Please enter the first parallel side's measure: "))
    b = float(input("Please enter the second parallel side's measure: "))

    area = 1/2 * h * (a + b)
   
    print('The area of the trapezium is', area, 'sq.units')

    again()
#Calculation for general quadrilateral 
def GQ():
    d = float(input("Please enter the diagonal of the quadrilateral: "))
    h1 = float(input("Please enter the first height's measure: "))
    h2 = float(input("Please enter the second height's measure: "))
   
    area = 1/2 * d * (h1 + h2)

    print('The area of the quadrilateral is', area, 'sq.units')
   
    again()
   #Calculation for parallelogram 
def parallelogram():
    b = float(input("Please enter the base of the parallelogram: "))
    h = float(input("Please enter the height of the parallelogram: "))

    area = b * h
   
    print('The area of the parallelogram is', area, 'sq.units')
   
    again()
 #Calculation for circle 
def circle():
    r =  float(input("Please enter the radius of the circle: ")) 
    pie = 3.14
    
    area = pie * r ** 2
    
    print('The area of the circle is', area, 'sq.units')
    
    again() 
 #For repeating the process   
def again():
    choice = input("Do you want to continue? Please type Y for yes or N for no: ")
    
    if choice == 'Y':
        calculate()
        
    elif choice == 'N':
        print("Bye! See you next time!") 
        
    else:
        again() 
        
calculate() 