list1=[[12,34,23],
       [3,5,4],
       [87,73,32]]

list2=[[12,343,43],
       [3,5,5],
       [1,4,2]]


list3=[[],[],[]]


for i in range(len(list1)):
    for j in range(len(list1[i])):
        list3[i].append(list1[i][j]*list2[i][j])


print(list3)
