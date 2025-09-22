myDictionary={"ali":"1 nov","vali":"2 nov","hasan":"3 nov"
              ,"husan":"4 nov","olim":"5 nov"}



name=input("Enter name of your friend : ").lower()

print(f"the birthday is on {myDictionary.get(name,'not found')}")