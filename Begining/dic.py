from turtle import TPen


mydic = {
    "name" : "Gayathra",
    "age" : "28",
    "color" : "Blue"
}

# print (mydic)
# print (type(mydic))

#copying a dic

# newdic = mydic.copy()
# print (newdic)


# another_dic = dict(mydic)
# print (another_dic)

# for x in mydic:
    # print (mydic[x])

# for x in mydic.values():
#     print (x)

# for y in mydic.keys():
    # print (y)

# for x, y in mydic.items():
    # print (x, y)

x = mydic.keys()
# print (x)
# print (type(x))

newdict = {
    "child1" : {
        "name" : "gayathra",
        "age" : "28"
    },
    "child2" : {
        "name" : "gayathri",
        "age" : "31"
    },
    "child2" : {
        "name" : "newboy",
        "age" : "25"
    }
}

# 
# print (newdict)

color1 = {
    "name" : "red",
    "code" : "010101"
}

color2 = {
    "name" : "blue",
    "code" : "50502"
}

color3 = {
    "name" : "green",
    "code" : "808154"
}

color_collction ={
    "c1" : color1,
    "c2" : color2,
    "c3" : color3
}

color_collction.update({"c1":color2})
print (color_collction)