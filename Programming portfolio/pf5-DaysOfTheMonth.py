months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31  
} #Dictionary containing months in numerical form and their number of days
x = int(input("Enter the month number: ")) #User inputs month number
if x >= 1 and x <=12: #Check if user input is in dictionary
    if x == 2: #Check if its february
        leap = input("If it is a leap year, enter y: ") #Ask if it's a leap year
        if leap == "y":
            months[2] = 29 #Change dictionary entry to appropriate number
    print("Month " + str(x) + " Has " + str(months[x]) + " days.")#Output month number and number of days
else:
    print("Invalid month.") #Output if user input is invalid