x, y, z = 1, 2, 3

# print (x)
# print (y)
# print (z)

# x = y = z = "orange"

fruits = ["orange", "mango", "apple"]
x, y, z = fruits

# print (x)
# print (y)
# print (z)

#use global keyword before the variable name inside a function to make it as a globally accessible one
def global_variable_check():
    global x
    x = 10

global_variable_check()

# print (x)


# String array
a = "hello world"

# print (a[0])
# print (a[6])

# tried wilth formatted string
poem = """Lorem ipsum dolor,
        sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua"""

# print (poem)

# checking the legth of a string
string = "apple is good"

# print (len(string))


# finding some text/phrase in a string line
x = "on one can do it"

print ("one" in x)