def tester(x): #Define function to test if even/odd
    y = x % 2 # Modulus of user input
    if y == 1: # If odd
        result = str(x) + " is odd" #Output if odd
    else: #If even
        result = str(x) + " is even" #Output if even
    return(result) # Return result when called

def main(): #Main body
    num = int(input("Enter a number: ")) # Ask user input
    print(tester(num)) #Call tester function and receive result

if __name__ == "__main__":
    main() #Call main function