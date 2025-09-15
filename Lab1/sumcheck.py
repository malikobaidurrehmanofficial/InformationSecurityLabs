a=[]
a.append(int(input("Enter num 1 : ")))
a.append(int(input("Enter num 2 : ")))
a.append(int(input("Enter num 3 : ")))
a.append(int(input("Enter num 4 : ")))

sumeven=0
sumodd=0

for i in a:
    if(i%2==0):
        sumeven=sumeven+i

    else:
        sumodd=sumodd+i


print(f"the sum of even numbers is {sumeven}  and sum of odd numbers is {sumodd}")


