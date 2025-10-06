print("\n\nNo.1")
dimensions = (10, 20, 30)
(length, width, height) = dimensions
print(length)

print("\n\nNo.2")
coordinates = (1.5, 2.5, 3.5)
(x, y, z) = coordinates
print(y)

print("\n\nNo.3")
person = ("John", 25, "Engineer")
(name, age, profession) = person
print("Profession:", profession)

print("\n\nNo.4")
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
student1 = data[0][0]
student2 = data[1][1]
print(student2)

print("\n\nNo.5")
colors = ("red", "green", "blue", "yellow")
color1 = colors[0]
color2 = colors[1]
print(color1)
print(color2)

print("\n\nNo.6")
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
(name, position, departments) = record
print(name)
print("Age:", position[0])
print("Department:", departments[0])

print("\n\nNo.7")
triplet = ("one", "two", "three")
(variable1, variable2, variable3) = triplet
print(variable2)

print("\n\nNo.8")
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
(product_ID, category, manufacture_date) = info
(type, price) = category
print(price)

print("\n\nNo.9")
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
(tuple1, tuple2, tuple3) = nested_tuple
print(tuple3[1])

print("\n\nNo.10")
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(apple, banana, cherry) = inventory
print("Quantity of banana:", banana[1])
