list=[1,45,25,78,34,23,90,11,10]


# using builtin methods

print(f"max value in the list is : {max(list)}")
print(f"min value in the list is : {min(list)}")

# without using builtin methods
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i

print(f"max value in the list is : {max}")
print(f"min value in the list is : {min}")