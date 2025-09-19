print("Enter 4 values for list one : ")

list1=[]

for i in range(0,4):
    list1.append((input()))


list2=[]

for i in range(0,4):
    list2.append((input("Enter 4 values for list two : ")))


print(f"appended list 1 and list 2 is : {list1+list2}")