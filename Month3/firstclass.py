# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# list1 = ["abc", 34, True]
# print(type(list1))

# list() constructor
# m = ("abc", 34, True)  
# my = list(m)
# print(my) 

# append - This adds to the end of a list (can only take one at once)
# thislist = ["apple", "banana", "cherry"]
# thislist.append(10)

# extend - Joins collections
# thislist1 = ["apple", "banana", "cherry"]
# thislist2 = ["orange", "kiwi", "melon", "mango"]
# thislist1.extend(thislist2)
# print(thislist1)

#remove, pop, del and clear can be used to remove an item from a collection
# thislist.sort()
# thislist.sort(reverse=True) #capital letter comes first
# thislist.sort(key=str.lower)

# thislist.reverse #from the back

# Tuple - immutable, indexed, ordered
# changing to list 
# Unpacking a Tuple
# Using asterick and underscore


# loop conditions
# i. declaratiom
# ii. condition
# iii. increment or decrement

# while (i=0; i < 5; i += 1){
#     print("hello")
# }

# i = 0
# while i < 5:
#     print("hello")
#     print(f'This is the {i}rd time ')
#     i += 1

# i = 0
# while i < 3:
#     print("Hello")
#     i += 1

# i = 0 
# while i <= 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# i = 0 
# while i < 10:
#     if i != 5:
#         print(i)
#     i += 1

# print("The password is passwod")
# while True:
#     m =  input("Put password here: ")
#     if m == "passwod":
#         print("Correct")
#     else:
#         print("Try again")