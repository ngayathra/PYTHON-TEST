thisset = {"apple", "banana", "cherry", "mango", "avacado"}
mylist = ["kiwi", "orange"]
mytuple = {"hi",}

thisset.update(mytuple)

thisset.update(mylist)
print (thisset)
print ("-----------------------------")

for x in thisset:
    print (x)