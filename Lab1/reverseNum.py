num=int(input("Enter a number to gets its reverse  :  "))


res=""

while num>0:
    res=res+str(num%10)

    num=num//10


print(f"The number is reverse format is : {res}")