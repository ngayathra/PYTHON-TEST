int_one = input("Please enter your name here ")
input_val_02 = input("Please enter your age here ")

# int_one = int(input_val_01)

# print (type(int_one))

def input_value_checkup():
    if int_one.isdigit() != 1:
        print ("You entered an String, Please enter a number here")
    else:
        new_int_one = int(int_one)
        if new_int_one > 0:
            print (f"the value you entered {new_int_one}")

        elif new_int_one == 0:
            print ("You entered zero value, Please enter a posotive number here")

input_value_checkup()