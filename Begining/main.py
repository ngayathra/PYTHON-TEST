from urllib.parse import uses_relative


calculation_to_units = 24
name_of_units = "hours"


"""
print (f"20 days are {20 * calculation_to_units} {name_of_units}")
print (f"35 days are {35 * calculation_to_units} {name_of_units}")
print (f"50 days are {50 * calculation_to_units} {name_of_units}")
print (f"110 days are {110 * calculation_to_units} {name_of_units}")

"""
def myfuncion(num_of_days):
    # print (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    # print (num_of_days >=0)
    conditional_check = num_of_days>=0
    print(type(conditional_check))
    if num_of_days >= 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    # print (custom_message)
    else:
        return "you entered a negetive value, so no result"


""""
def scope_check():
    another_value = "1"
    num_of_days = 2
    print (calculation_to_units)
    print (another_value)
    print (num_of_days)

myfuncion(15, "hello")
myfuncion(20, "wow")
scope_check()
"""

# int(user_input()) = 1

# user_input = input("Hey user, enter a number of days and I will convert it to hours\n")
# user_input_number = int(user_input)

# calculated_value = myfuncion(user_input_number)
# print (calculated_value)


print(type(10.2))
