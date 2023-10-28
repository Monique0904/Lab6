
# creates a function to print the menu and ask the user for their menu selection
def main():

    print("\nMenu\n-------------\n1.Encode\n2.Decode\n3.Quit")
    global user_op
    user_op = int(input("\nPlease enter an option:"))

    return user_op

# encodes the given password
def encode(passw):

    # if the inputted password is not 8 chr long then an error is raised
    if len(passw) > 8 or len(passw) < 8:
        raise ValueError("Must be 8 characters")

    password = []

    # iterates through each chr, if it's a digit it will be increments by 3 turned into a str and added to the list
    for i in passw:
        if 48 <= ord(i) <= 57:
            password.append(str(int(i) + 3))
        # if the password has anything other than na digit an error is raised
        else:
            raise ValueError("Must only contain integers")

    return ''.join(password)

def decode(passw):
    pass

while True:

    try:
        # prints menu and returns users menu option
        main()

        # depending on user option, the statements bellow will either encode, decode, exit the loop, or loop again
        if user_op == 1:
            encoded_pass = encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")

        elif user_op == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.")

        elif user_op == 3:
            break

        else:
            print("Invalid menu option")

    # if the ValueError is raised in any of the functions the message attached to the error will print
    except ValueError as expt:
        print(expt)



