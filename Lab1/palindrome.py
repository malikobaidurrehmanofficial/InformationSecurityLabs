a=input("Enter a string to check is it palindrome or not : ")
palindrome=""
for i in a:
    palindrome=i+palindrome


if a==palindrome:
    print("yes it is palindrome")
else:
    print("No it is not a palindrome")