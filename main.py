def add_num(val_num):
    var_num = 5
    return var_num + val_num


def validate_and_execute():
    try:  # lets you test a block of code for errors
        user_input_val = int(num_of_elements)
        if user_input_val > 0:  # nested if
            final_val = add_num(user_input_val)  # casting
            print(final_val)
        elif user_input_val <= 0:
            print('Enter a valid number')
    except ValueError:  # catches the error and lets you handle it
        print('The input is not an integer')


user_input = ""  # assign an empty string to the user input
while user_input != "exit":  # Condition gets evaluated
    user_input = input("Enter the value of the number\n")
    for num_of_elements in user_input.split(", "):
        validate_and_execute()  # User is prompted for input
