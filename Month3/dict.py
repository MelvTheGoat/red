print("\n\nNo.1")
family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
print(family["children"][1]["age"])

print("\n\nNo.2")
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Python 101"]["author"] = "Mike"
print(library)
