# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to extract
keys = ["name", "salary"]

# Method 1: Using dictionary comprehension
new_dict = {key: sample_dict[key] for key in keys}
print("Method 1 - Dictionary Comprehension:", new_dict)

# Method 2: Using a for loop
new_dict2 = {}
for key in keys:
    new_dict2[key] = sample_dict[key]
print("Method 2 - For Loop:", new_dict2)

# Method 3: Using the dict() constructor with a generator expression
new_dict3 = dict((key, sample_dict[key]) for key in keys)
print("Method 3 - Dict Constructor:", new_dict3)