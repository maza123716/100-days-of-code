def add_num(val_num):
    var_num = 5
    return var_num + val_num


def validate_and_execute():
    user_input = ""  # assign an empty string to the user input
    while user_input != "exit":  # Condition gets evaluated
        user_input = input("Enter the value of the number\n")
        try:  # lets you test a block of code for errors
            if int(user_input) > 0:  # nested if
                final_val = add_num(int(user_input))  # casting
                print(final_val)
            elif int(user_input) <= 0:
                print('Enter a valid number')
        except ValueError:  # catches the error and lets you handle it
            print('The input is not an integer')


validate_and_execute()  # User is prompted for input
