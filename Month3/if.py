# a = int(input("Put a number: "))
# b = int(input("Put a number: "))

# if a and b >= 1:
#     print("a and b are both positive")
# elif a or b < 1:
#     print("Only one is positive")
# else:
#     print("Neither is positive")



# palindrome = str(input("Enter a word: "))

# if palindrome == palindrome[::-1]:
#     print("Is a palindrome")
# else:
#     print("Not a palindrome")

# x = input("Enter variable: ")
# y = input("Enter variable: ")
# z = input("Enter variable: ")
# if x == y == z: 
#     print("All same")
# elif x==y or x == z or y == z or y == x:
#     print("Two are equal")
# else: 
#     print("All different")


# colors input("here:")
# colors = ["red", "blue", "yellow"]
# (color1, color2, color3) = colors
# if color1 == color2 == color3:
#     print("All primary colors") 
# else:
#     print("Not all primary colors")


# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# i = 0
# while i < len(names) and i < len(grades):
#     print(f'{names[i]}  got grade {grades[i]}')
#     i += 1

# mode = ["manual", "automatic", "off"]
# mode = input("mode: ")
# if mode == "manual":
#     print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# else:
#     print("System is off")


# message = ["urgent", "important", "immediate"]
# text = input("message: ")
# if text == message:
#     print("High priority message")
# else:
#     print("Normal message")

# fruits = ['apple', 'zebra', 'mango', 'lemon']
# newfruits = any([x.startswith('z') for x in fruits])
# print(newfruits)

# Input = ["banana", "mango", "kiwi", "grape"]
# vowels = "aeiou"
# newinput = all([v.endswith(vowels) for v in Input])
# print(newinput)

# cap = ["HELLO", "WORLD", "PYTHON"]
# newcap = [x.lower() for x in cap]
# print(newcap)

# temp = [12, 7, 3, -1, 5]
# newtemp = all([t > 0 for t in temp])
# print(newtemp)

# numbers = [5, -2, 3, 0, 8]
# newnum = any([numb < 0 for numb in numbers])
# print(newnum)

# num_multi = [2, 4, 6, 8]
# multi = [n * 3 for n in num_multi]
# print(multi)

# nature = ["sky", "tree", "rock", "stone"]
# newnature = []
# for e in nature:
#     if 'e' in e:
#        newnature.append(e)
# print(newnature)

# names = ["Alice", "Bob", "charlie", "David"]
# newname = all([name.isupper() for name in names])
# print(newname)


# password = input('Enter password: ')
# spec_char = '!@#$%^&*()'
# number = '1234567890'
# upper = 'QWERTYUIOPASDFGHJKLXZCVBNM'
# lower = 'qwertyuiopasdfghjklzxcvbnm'
# newpassword = any([num in password for num in number] and [char in password for char in spec_char] and [up in password for up in upper] and [low in password for low in lower])
# if newpassword == False:
#     print('Try again')
# elif newpassword == True: 
#     print("Correct")
# print(newpassword)

# def square_root(num):
#    print(f'Square Root is: {num**1/2}')


# No. 1
# def turn_to_upper(names):
#     return [names.upper() for names in names]
# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))

# # No. 3
# def reverse_string(string):
#     return string[::-1]
# print(reverse_string('MelvTheGoat'))

# No. 6
# def find_max(number):
#     return max(number)
# print(find_max([12, 45, 3, 67, 23, 100]))

# # No. 7
# def sum_dict_values(dict):
#     return sum(dict.values())
# print(sum_dict_values({"a": 10, "b": 20, "c": 5}))

# # No. 9
# def is_palindrome(palindrome):
#     return palindrome == palindrome[::-1]
# print(is_palindrome("Melvyn"))
# print(is_palindrome("Level"))

# # No. 13
# def power(base, exponent=2):
#     return base**exponent
# print(power(4))
# print(power(2, 3))

# # No. 2
# def get_middle_name(name_dict):
#     return name_dict["Middle"]
# come back
# print(get_middle_name(name_dict))








# # No. 3
# def multiply_first_two(*num):
#     return num[0] * num[1]
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# # No. 5
# def total_age(*age):
#     return sum(age)
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# # No. 6
# def list_countries(*countries):
#     for country in countries:
#         print(country)
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# No. 8
# def average_score(*scores):
#     return sum(scores) / len(scores)
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# No. 13
# def find_min(*numb):
#     return min(numb)
# print(find_min(99, 45, 12, 88))
# print(find_min(8, 3, 7))


# def total_price(**item):
#     return sum(item.values())
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))


# def first_and_last(fl):
#     return f'{}'
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")


# def greet_user(first_name, last_name="") :
#     return f'{first_name} {last_name}'

# print(greet_user("Ada"))
# print(greet_user("Tola", "Akin"))