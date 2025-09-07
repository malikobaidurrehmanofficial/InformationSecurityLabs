num=int(input("Enter any number to get sum upto it except 0(zero is for termination) :  "))
sum=0
while num !=0:
    sum+=num
    num=int(input("Enter any number to get sum upto it except 0(zero is for termination) :  "))


print(f"sum of numbers is : {sum} ")