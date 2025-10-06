# Loops in python
# A loop in programming would repeatedly executes a block of code as long as a specified condition is true. 
# i += 1
# print('Hello world')
# The while loop
# i. Declaration
# ii. Condition
# iii. Increment or decrement value 

# while (i = 0  ;  i< 5 ; i += 1) {

# }

# i = 0
# while i < 5:
#     print('Hello world')
#     print(f'This is the {i} time\n')
#     i += 1

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# i = 1
# while i <= 12:
#     print(f'2 X {i} = {2*i}')
    # i += 1

# The break statement 
# used to quit the loop even when the condition is still true 

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# The continue statement 
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# The while...else 
# i = 1
# while i <= 12:
#     print(f'2 X {i} = {2*i}')
#     i += 1
#     if i == 7:
#         break
# else:
#     print('The multiplication of 2')
# when loop quits naturally, it does whatever is in the else block 
# but if loop should quit using a break statement, it skips the else block 
# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

# print('THe password is passwod')
# while True:
#     m = input('Please enter the password : ')
#     if m == 'passwod':
#         print('Correct!!!')
#         break
#     else:
#         print('Wrong, please try again!')

# mylist = ['start','stop','end','replay']
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i += 1

# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# import random
# rsn = random.randint(1,50)
# i = 0
# while i < 5:
#     num = int(input('Please enter the secret number : '))
#     if num > rsn:
#         print('Guess too high, try again!!')
#     elif num < rsn:
#         print('Guess too low, try again!!!')
#     else:
#         print('Correct!!\nYou got it correctly')
#         break
#     i += 1
# else:
#     print('Maximum attempt reached')
#     print(f'The number is {rsn}')


# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

# bs = int(input('Enter the base : '))
# exp = int(input('Enter the exponent : '))
# exp1 = exp
# rsp = 1
# while exp > 0:
#     rsp *= bs
#     exp -= 1
# print('Output:')
# print(f'{bs} raised to the power of {exp} is {rsp}')

# user = int(input('Please enter the number : '))
# sum = 0
# while user > 0:
#     print(user)
#     sum += user
#     user -= 1
# else:
#     print(f'The sum of all natural numbers up to that number is {sum}')

# user = int(input('Please enter the number : '))
# sum = 0
# i = 1
# while user > 0:
#     sum += i
#     user -= 1
#     print(i,end=',')
#     i += 1
# else:
#     print(f'The sum of all natural numbers up to that number is {sum}')

# vowel = 'aeiou'
# count = 0
# word = input('Please enter word to check vowel: ')
# lenword = len(word)
# i = 0
# while lenword > 0:
#     if word[i].lower() in vowel:
#         count += 1
#     lenword -= 1
#     i += 1

# print(count)

# print('The end is near',end=' ')
# print('11112q')

# user = input('Please enter the word : ')
# i = -1
# lenuser = len(user)
# while lenuser > 0:
#     print(user[i],end='')
#     i -= 1
#     lenuser -= 1

# Write a program that takes comma-separated integers from the user, converts that
#   to a tuple and uses a while loop to find the minimum value in the tuple. Do not Use the min() function.
# user = '34,77,2'
# inputlist = user.split(',')
# print(inputlist)
# x,y,z = inputlist
# x,y,z = int(x),int(y),int(z)

# tupleinput = (x,y,z)
# i = 0
# x = tupleinput[0]
# while i < len(tupleinput):
#     if tupleinput[i] < x :
#         x = tupleinput[i]
#     i += 1
    
# print(x)
# user = '34,77,2'
# inputlist = user.split(',')
# print(inputlist)
# x = tuple(inputlist)
# i = 0
# y = int(x[0])
# while i < len(x):
#     if int(x[i]) < y:
#         y = int(x[i])
#     i += 1



# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# balance = int(input('Enter your balance: '))
# while True:
#     withdrawal = int(input('Enter withdrwal amount : '))
#     if withdrawal > balance:
#         print('You cannot withdraw more than your balance')
#         continue
#     else:
#         balance -= withdrawal
#         print(f'Remaining balance: {balance}')
#     choice = input('Do you want to make another withdrawal? (yes/no) : ').lower().strip()
#     if choice == 'yes':
#         continue
#     elif choice == 'no':
#         print(f'Final balance {balance}')
#         break
#     else:
#         print('Didn\'t get that, quitting....') 
#         break




# Loop - For loops 
# used to iterate directly  over items of a sequence or other iterable object, making them more intuitive and flexible

# for item in [1,2,3]:
#     print(item)

# Looping through different data types in for loop
# cities = ["New York", "Paris", "Tokyo", "Sydney", "Cairo"]

# for i in cities:
#     print(f"City: {i}")

# items = ("guitar", "keyboard", "drums", "microphone", "amp")
# for item in items:

#     print(f"Item: {item}")

# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}

# for country in capitals:
#     print(f"Country: {country}")

# for y in capitals.values():
#     print(f"Kapital: {y}")

# for x,y in capitals.items():
#     print(f'Country {x} for capital {y}')

# books = {"1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "Pride and Prejudice"}
# for book in books:
#     print(f"Book: {book}")

# Even strings are iterable objects, they contain a sequence of characters:
# my_string = "Python is fun!"
# for char in my_string:
#     print(f"Character: {char}")


# my_string = "Python is fun!"
# i = 1
# for char in my_string:
#     if i == 3:
#         print(f"Character: {char}")
#     i += 1

# the break statement 
# actions = ["run", "jump", "stop", "walk"]
# for x in actions:
#   print(x)
#   if x == "stop":
#     break
  
# for x in actions:
#     if x == "stop":
#         break
#     print(x)

# The continue statement 
# tasks = ["start", "process", "skip", "finish"]
# for x in tasks:
#     if x == "skip":
#         continue
#     print(x)

# The range function in a loop 
# x = range(0,10,2)
# for a in x:
#     print(a)

# for b in range(2,9):
#     print(b)

# for a in range(5):
#     print('Hello')

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# for x in range(6):
#   if x == 3: 
#     break
#   print(x)
# else:
#   print("Finally finished!")

# The enumerate function in python adds a counter to an iterable and returns it as an enumerate object. This allows  us to loopover the iterable and have access to both the index and the value of each item simultaenoulsy.

# fruits = ['apple', 'banana', 'cherry']
# for i, f in enumerate(fruits, start=0):
#     print(f"{i}: {f}")

# my_string = "Python is fun!"
# i = 1
# for char in my_string:
#     if i == 3:
#         print(f"Character: {char}")
#     i += 1

# for i, char in enumerate(my_string, start = 1):
#     if i == 3:
#         print(f'Character {char}')

# The pass statement 
# for x in [0, 1, 2]:
#     pass

# Nested Loops 
# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)

# Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]
# a = "1, 2, 3, 2, 4, 3"
# b = a.split(',')
# print(b)
# print(type(b))

# c = []
# d = []
# for x in b:
#     if x in c:
#         continue
#     else:
#         c.append(x)

# print(c)
# for x in b:
#     if x not in d:
#         d.append(x)

# print(d)

# Write a program that takes an integer n from the user and calculates the sum of 
#   squares of all numbers from 1 to n. Print the sum. Example:
#   Input: 3
#   Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input('Please enter the number : '))
# sum = 0
# for a in range(1,n+1):
#     a *= a
#     sum += a

# print(sum)

# Given two lists of numbers of the same length, print the indices and values
#   of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]
# for i,a in enumerate(list1,start=0):
#     if a == list2[i]:
#         continue
#     else:
#         print(f'Index {i}: {a} != {list2[i]}')

# List comprehensions - lc in python, provides a concise way to create list from another list. They consis of brackets containing an expression followed by a for clause, and can also incude optional if clauses to filter items.

# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City", 'Lagos']
# newlist = []
# for a in cities:
#     if 'a' in a.lower():
#         newlist.append(a)

# print(newlist)

# newcities = [city for city in cities if 'a' in city.lower()]
# print(newcities)

# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# a = ['Hello' for city in cities]
# print(a)
# a = [city for city in cities if city != 'Lagos']
# print(a)

# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x % 2 == 0 and x != 0]
# print(newlist)

# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# newlang = [a.upper() for a in languages]
# print(newlang)

# Other comprehension 
# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# newset = {x for x in languages}
# print(newset)

# newdict = {x:len(x) for x in languages}
# print(newdict)

# any()  and all()
# any(): Returns True if at least one element in the iterable is True, otherwise False.
# all(): Returns True if all elements in the iterable are True, otherwise False.

# anyexample = any([x>3 and x>7 for x in range(1,6)])
# print(anyexample)

# allexample = all([x > 3 for x in range(3,10)])
# print(allexample)

# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# expected output: True 
# correction 
# v = ["apple", "zebra", "mango", "lemon"]
# x = any([x.startswith('z') for x in v])
# print(x)

# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
# words = ["hi", "dog", "go", "sun"]

# Python Functions 
# a function is a block of code that performs a specific task.

# def greet():
#     print('Hello world')
#     print('Welcome to python')

# greet()

# print('Python is fun')
# print(2 + 6)

# greet()
# greet()

# Parameters are the variables listed inside the parentheses in the function 
# definition. They act like placeholders for the data the function can accept when 
# we call them.

# Think of parameters as the blueprint that outlines what kind of information the function expects to receive.

# def ope(name):
#     print(f'Welcome {name}')
#     print('Python is fun')

# ope('Titi')
# parameters are placeholders for arguments  

# def five_years_age(num):
#     print(f'in 5 years time, you\'d be {num + 5}')

# five_years_age(40)

# user = int(input('Please enter your current age : '))
# five_years_age(user)

# def sum_numb(num1,num2):
#     print(f'The sum of the number is {num1+num2}')

# sum_numb(2,4)

# The return statement - we return a value from the function using the return statement
# def sqrt(num,num1):
#     return num ** 0.5

# def sqrta(numb):
#     print(numb**0.5)

# m = sqrt(49)
# print(sqrt(25))

# THe pass statement 
# The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.

# It's typically used where code is planned but has yet to be written.

# Default Arguments in Functions 
# Python allows functions to have default argument values. Default arguments are used when no explicit values are passed to these parameters during a function call.

# def greet(name, message='Hello'):
#     print(message, name)

# greet('Ope')
# greet('Iyanu','Good morning')

# Using a mutable default value (like a list or dictionary) in function definitions can lead to unexpected behavior because the default value is shared across all calls to the function.

# Example:
# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# print(add_item(1))
# print(add_item(2))

# Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.

# def change(mylist):
#     new = {}
#     for a in mylist:
#         new[a] = len(a)
#     return new

# print(change(["apple", "banana", "cherry"]))

# Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying
# a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0

# def calculate_discount(price, discount=10, tax=0):
#     discountedprice = price*((discount/100))
#     discountprice = price - discountedprice
#     taxx = tax/100
#     taxprice = discountprice * (taxx)
#     finalnewprice = discountprice + taxprice

#     return finalnewprice

# print(calculate_discount(200, discount=20, tax=5))
# print(calculate_discount(100))

