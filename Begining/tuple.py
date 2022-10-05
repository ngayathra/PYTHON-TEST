first_tuple = ("apple",)
# print (first_tuple)
# print (type(first_tuple))

second_tuple = ("apple", "banana", "cherry", "apple", "cherry")

#checking the tuple length
# print (second_tuple)
# print (len(second_tuple))
# print ("-------------------------------------")

#creating a tuple with it's constructor
constructor_tuple = tuple(("apple", "banana", "cherry", "apple", "cherry"))

# print (constructor_tuple)


#checking an item in a tuple
if "chery" in second_tuple:
    print ("yes we got it")
else:
    print ("no we did't get it")


#copying a tuple to a list
tuplelist = list(second_tuple)
# print (type(tuplelist))
# print (tuplelist)
