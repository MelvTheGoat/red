# i = 1
# while i <= 10:
#     print(i) 
#     i += 1

# i = 2
# n = int(input('Number here: '))
# while i <= n:
#     print(i)
#     i += 2




# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# i moved here variable into the while and it worked. why?
# while True:
#     here = input('Password here: ')
#     if here == "secret":
#         print('Correct')
#         break
#     else:
#         print('Try again')


# n = int(input('Number here: ')) 
# while n >= 0:
#     print(n)
#     n -= 1


# vowels = 'aeiou'
# word = str(input('Put word here: '))

# count = 0
# i = 0
# while i < len(word):
#     if word[i] in vowels: 
#         count += 1
#     i += 1
# print(f'number of vowels {count}')


# Write a program that uses a while loop to print numbers from 1 to 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1 

# Sum of natural numbers up to n
# n = int(input("Number here: "))
# i = 1
# count = 0

# while i <= n:
#     count += 1
#     i += 1

# print("addition", count)


# password = ''
# while password != "secret":
#     password = input('here: ')
# print("Correct")




# n = int(input("Number here: "))

# while n >= 0:
#     print(n)
#     n -= 1

# n = int(input("Enter a number: "))
# i = 2

# while i <= n:
#     print(i)
#     i += 2



# balance = int(input("Enter balance here: "))
# while True:
#     withdrawal = int(input("Enter Withdrawal Amount: "))
#     if balance <= 0:
#         print("Balance too low")
#         break
#     elif balance > withdrawal:
#         balance -= withdrawal
#         print(f'Remaining balance: {balance}')
#     choice = input("Do you want to make another withdrawal? (yes/no): ")
#     if choice == 'yes':
#         continue
#     elif choice == 'no':
#         print(f'Final balance: {balance}')
#         break
#     else:
#         print("input 'yes' or 'no'")




# total = 0
# while True:
#     price = float(input("Enter item price: $"))
#     if price > 0:
#         total += price

#     choice = input("Enter another item? (yes/no): ")
#     if choice == 'yes':
#         continue
#     elif choice =='no':
#         print(f'Total cost: ${total}')
#         break
#     else:
#         print("input 'yes' or 'no'")



# while True:
#     password = str(input('Enter password here: '))
#     if len(password) > 8 and len(password) < 25:
#         print('Password accepted')
#         break
#     else:
#         print('Password must be at least 8 characters long and have a maximum of 25 characters.')

# for h in range (0, 5):
#     h = 'hello'
#     print(h)
        
# for h in range (0, 5):
#     print('hello')

# No. 1
# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

sum = 0
n = int(input('Enter number here: '))

while n > 0:
    digit = n%10
    sum += digit
    n //= 10
print(f'Total: {sum}')

# No. 2 
# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

n = str(input('Enter word here: '))
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
i = 0

while len(n) > 0:
    if n[i] in vowels or consonants:
        print()


