my_list = ["jan", "feb", "march", "april"]
second_list = ["rice", "nasi", "curry"]
third_list = second_list.copy()

my_list.append("dec")


list3 = my_list + second_list
print (list3)

second_list.extend(my_list)
print (second_list)

for x in my_list:
    third_list.append(x)

third_list.reverse()
print(third_list)


third_list.clear()
print(third_list)




# print (my_list[4])
# new_list = ""
# for x in my_list:
    # print(x)
# my_list.append("MAY")
# my_list.insert(2, "gayatra")
# my_list.extend(second_list)

# print (my_list)


# [print(x) for x in my_list]
# for x in my_list:
#     print (x)

# for i in range(len(my_list)):
#     print (my_list[i])

# x = 0
# while x < len(my_list):
#     print (my_list[x])
#     x = x + 1

newlist = ["orange", "mango", "kiwi", "pineapple", "banana"]

anotherlist = []

# for x in newlist:
#     if "a" in x:
#         anotherlist.append(x)
# print (anotherlist)
# x = 1
# while x < 31:
#     print (f"{x}/09")
# #     x = x +1
# print (newlist)
# newlist.sort(reverse=True)
# print (newlist) 

# copylist = newlist.copy()
# print (copylist)

# clist = list(newlist)
# print (clist)
