a=input("Enter a string to check is it palindrome or not : ").lower()
palindrome=""
for i in a:
    palindrome=i+palindrome


if a==palindrome.lower():
    print("yes it is palindrome")
else:
    print("No it is not a palindrome")