password = "12345" # Create password
for i in range(1,6): # Limit number of attempts
    entry = str(input("Enter the password: ")) # User input password
    attempts = 5 - i # Calculate number of attempts left
    if entry == password: # Check if password is correct
        print("Access granted!") #Output if password is correct
        break                    #Leave loop
    else:
        print("Access denied!\nYo have " + str(attempts) + " left") #Output if password is incorrect