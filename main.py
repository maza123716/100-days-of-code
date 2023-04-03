name = "Joan"
age = 23
# data = "%s is %d years old" % (name, age)
print(f'{name} is {age} years old')

data = "John", "doe", 53.44
format_string = "Hello %s %s, your balance is %f" % data
print(format_string)

astring = "Hello world!"
# prints out the location of the first occurrence  of letter w
print(astring.index("d"))

string = "Hello world!"
# prints out the number of l's in the string
print(string.count("l"))

a_string = "Hello world!"
print(a_string[3:7])

# for loop
prime = [1, 2, 4, 5]
for x in prime:
    print(x)

# while loop
count = 0
while count <= 5:
    print(count)
    count += 1

print(200)

# string concatenation
# global function (defined within any scope)

# calculation_to_units = 24 * 60
# name_of_unit = "minutes"
# print(f'20 days are {to_minutes} {name_of_unit}')
# print('20 days are' + ' ' + str(to_minutes) + ' ' + name_of_unit)


# function


# def days_to_units():
# print(f'20 days are {to_minutes} {name_of_unit}')
# print('20 days are' + ' ' + str(to_minutes) + ' ' + name_of_unit)


# days_to_units()


# function parameters

def days_to_units(num_of_days, custom_message):  # local variables (defined within the function)
    calculation_to_units = 24 * 60
    name_of_unit = "minutes"
    print(f'{num_of_days} days are {calculation_to_units * num_of_days} {name_of_unit}')
# print(f'{num_of_days} days are' + ' ' + str(to_minutes) + ' ' + name_of_unit)
    print(custom_message)


days_to_units(20, "Looks good")
days_to_units(35, "Awesome!")


def create_var():
    inside_var = "Variable inside function"
    print(inside_var)


create_var()


# function with return values


def return_val(y):
    return 5 * y


print(return_val(3))
print(return_val(4))
print(return_val(7))


# user input

# To ask the user for an input


# user_input = input("Hey user enter number\n")
# print(user_input)


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
