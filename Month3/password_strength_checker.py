# while True:
#     password = input('Enter password: ')
#     spec_char = '!@#$%^&*()'
#     num = '1234567890'
#     upper = 'QWERTYUIOPASDFGHJKLXZCVBNM'
#     lower = 'qwertyuiopasdfghjklzxcvbnm'
#     if(
#         len(password) > 8
#         and any(char in spec_char for char in password)
#         and any(number in num for number in password)
#         and any(upper_letter in upper for upper_letter in password)
#         and any(lower_letter in lower for lower_letter in password)
#     ):
    # if len(password) > 8 and spec_char[i] in password and num[d] in password and upper[i] in password and lower[l] in password:
    #     print('True')
    # else:
    #     print('False')










# No. 3
n = int(input("Enter a number: "))
i = 1
while i <= 12:
    print(f"{n} x {i} = {n*i}")
    i += 1


# No. 8
n = int(input("Enter n: "))
i = 2
t = 0
while i <= n:
    t += i
    i += 2
print("Sum of even numbers =", t)


# No. 10
n = int(input("Enter n: "))
i = 1
t = 0
while i <= n:
    t += i * i
    i += 1
print("Sum of squares =", t)


# No. 14
for x in range(2, 21, 2):
    print(x)

# No. 18
names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
grades = ['A', 'E', 'F', 'C', 'B']
i = 0
while i < len(names) and i < len(grades):
    print(f"{names[i]} got grade {grades[i]}")
    i += 1


# No. 19
items = ['shoe', 'stick', 'toy', 'fruit']
i = 0
while i < len(items):
    if i % 2 == 0:
        print(f"{i}: {items[i]}")
    i += 1

 # No. 2 
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
vowel_no = 0
consonant_no = 0
while i < len(text):
    ch = text[i]
    if ch.isalpha():
        if ch in vowels:
            vowel_no += 1
        else:
            consonant_no += 1
    i += 1
print("Vowels:", vowel_no)
print("Consonants:", consonant_no)


# No. 4
word = input("Enter string here: ")
i = len(word) - 1
backwords = ""
while i >= 0:
    rev += word[i]
    i -= 1
print("Reversed string:", backwords)

# No. 6
n = int(input("Enter number: "))
a, b = 0, 1
i = 0
while i < n:
    print(a)
    a, b = b, a + b
    i += 1

# No. 9
# Come back to chekc again
s = input("Enter a string: ")
freq = {}
i = 0
while i < len(s):
    ch = s[i]
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
    i += 1
keys = list(freq.keys())
j = 0
while j < len(keys):
    k = keys[j]
    print(f"{k}: {freq[k]}")
    j += 1

# No. 11
phrase = input("Enter a phrase: ")
words = phrase.split()
i = 0
acronym = ""
while i < len(words):
    if words[i]:
        acronym += words[i][0].upper()
    i += 1
print(acronym)

# No. 12
s = input("Enter a string: ").strip()
if s == "":
    print("Word count: 0")
else:
    words = s.split()
    print("Word count:", len(words))

# No. 19
items = ['shoe', 'stick', 'toy', 'fruit']
i = 0
while i < len(items):
    if i % 2 == 0:
        print(f"{i}: {items[i]}")
    i += 1





# i = -1
# text = input('Enter text: ')
# vowels = 'aeiou'
# consonants = 'qwrtypsdfghjklzxcvbnm'

# user = input('Please enter the word : ')
# i = -1
# lenuser = len(user)
# while lenuser > 0:
#     print(user[i],end='')
#     i -= 1
#     lenuser -= 1


#  No. 7
# num = input('Enter here: ')
# number = num.split(",")
# print(number)

# No. 9
# text = input("Enter here: ")
# frequency = {}
# i = 0
# while i < len(text):
#     letter = text[i]
#     if letter in frequency:
#         frequency[letter] += 1
#     else:
#         frequency[letter] = 1 


names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
grades = ['A', 'E', 'F', 'C', 'B']
i = 0
while i < len(names) and i < len(grades):
    print(f'{names[i]} got grade {grades[i]}')
    i += 1