a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ] 
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]

c=[]
for i in range(0,len(a)):
    d=[]
    for j in range(0,len(a[i])):
        d.append(a[i][j]*b[i][j])
    
    c.append(d)

print(c)