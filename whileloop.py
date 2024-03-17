while True:
    zip = input("enter zip code: ")
    a = len(zip.strip())
    b = zip.isdigit()
    if a == 5 and b:
        print("valid zip code")
        break
    else:
        print("please enter a valide zip code")

"""email_address = input("enter your email: ")
if '@' in email_address:
    print("email valid")
else: 
    print("Invalide email")"""