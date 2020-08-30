#Importing Calendar:
def calendar():
#To import calendar 
     import calendar

#Input from user
     yy = int(input("Please enter the year:"))
     mm = int(input("Please enter the month in numbers:"))

#To print the calendar
     print(calendar.month(yy, mm))
     again() 
def again():
    choice = input("Do you want to continue? Please type Y for yes and N for no:")

    if choice.upper() == 'Y':
        calendar()

    elif choice.upper() == 'N':
        print("Bye! See you later!") 
 
    else:
        again() 

calendar() 
