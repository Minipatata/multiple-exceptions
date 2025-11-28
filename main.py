try:
    string1_user=str(input("Enter a string: "))
    string2_user=str(input("Enter another string: "))
    print("Your strings are: ",string1_user, string2_user)
except Exception as e:
    print("error occured",e)
finally:
    print("Wow, your strings are soooo good user!")