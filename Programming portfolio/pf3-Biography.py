dict1 = {
    "First name" : "N/A",
    "Surname" : "N/A",
    "Age" : 0,
    "Hometown" : "N/A"
} #Create empty dictionary
age = 0 #Declare variable age and set it to 0
while True: #Open loop
    dict1["First name"] = input("Enter your first name: ")
    dict1["Surname"] = input("Enter your Surname: ")
    age = input("Enter your age: ")
    dict1["Hometown"] = input("Enter your hometown: ") # Ask user input for dictionary
    if age.isdigit(): #Check if age is a valid input
        break #Exit loop if age is valid
    else:
        print("Invalid age. Try again") # Output if invalid input
dict1["Age"] = age # Set dictionary "Age" to user input
print("My name is " + dict1["First name"] + " " + dict1["Surname"] + "\nI am " + str(dict1["Age"]) + " years old" + "\nMy hometown is " + dict1["Hometown"])
#Print all dictionary entries with appropriate text