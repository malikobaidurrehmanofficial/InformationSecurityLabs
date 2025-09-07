num=int(input("Enter any number to check weather is it prime or not :  "))


isPrime=False


isPrime = True  
for j in range(2, (num // 2) + 1):
    if num % j == 0:
        isPrime = False
        break

if isPrime==True:
    print(f"the number {num} is prime ")

else:
    print(f"the number {num} is not prime ")