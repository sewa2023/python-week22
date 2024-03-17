"""my_string = input("Enter a string: ")
a = len(my_string.strip())

print(f"the string entered is: {a} characters")"""
try:
    a = int(input("enter integers: "))
    b = int(input("enter integers: "))
    sum = a + b
    print(sum)
except ValueError:
    print("Invalid input! Please enter intergers only")