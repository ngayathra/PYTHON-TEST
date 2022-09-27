calculation_to_units = 24
name_of_units = "hours"


"""
print (f"20 days are {20 * calculation_to_units} {name_of_units}")
print (f"35 days are {35 * calculation_to_units} {name_of_units}")
print (f"50 days are {50 * calculation_to_units} {name_of_units}")
print (f"110 days are {110 * calculation_to_units} {name_of_units}")

"""

def myfuncion(num_of_days, custom_message):
    print (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    print (custom_message)

def scope_check():
    another_value = "1"
    num_of_days = 2
    print (calculation_to_units)
    print (another_value)
    print (num_of_days)


myfuncion(15, "hello")
myfuncion(20, "wow")
scope_check()