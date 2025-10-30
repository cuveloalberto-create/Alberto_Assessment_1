names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] #Create a list of names
x = str(input("Enter a name: ")) # User input
if x in names: #Check if user input is in list
    print("Yes, " + x + " is in the list") # Output if name is in list
else:
    print("No, " + x + " is not in the list") # Output if name is not list