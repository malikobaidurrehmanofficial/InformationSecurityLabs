list1=[]
list2=[]
for i in range(0,4):
    list1.append(int((input("Enter 4 values for list one : "))))

for i in range(0,4):
    list2.append(int((input("Enter 4 values for list two : "))))

print(list1)
print(list2)

list3=list1+list2
list3.sort()

print(f"appended list 1 and list 2 in sorted order  is : {list3}")
