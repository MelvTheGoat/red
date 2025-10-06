# # 20
# print("Hello")
# ages = [25, 35, 20]
# ages.sort()
# print(ages) 

# # 21
# words = ["Apple", "banana", "Orange"]
# words.sort(key=str.lower)
# print(words)

# # 22
# numbers = [1, 2, 3, 4]
# numbers.sort(reverse=True)
# print(numbers)

# # 23
# letters = ["a", "b", "c", "d"]
# print(letters[::-1])

# # 24
# items = ["one", "two", "three"]
# item = items.copy()
# print(item)

# # 25
# list1 = ["a", "b"]
# list2 = ["c", "d"]
# list1.extend(list2)
# print(list1)

# # 26
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# print(data[0][2][1])

# # 27
# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# print(records[1][1][0])

# # 28
# group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
# female = group([0][0])
# print(female.find('e'))


students = {'name': 'John', 'age': '20', 'grade': 'A'}
print(students['name'])

product = {'name': "Laptop", 'price': 999.99 , 'stock': 50}
product['price'] = 899.99
print(product)

employee = {"name": "Alice", "position": "Manager"}
employee.update(salary=50000)
print(employee)

inventory = {"apple": 10, "banana": 5, "orange": 8}
del inventory['banana']
print(inventory)

person = {"name" : "Bob", "age": 25, "city": "New York"}
person_copy = dict(person)
print(person_copy)