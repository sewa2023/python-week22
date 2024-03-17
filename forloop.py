num_vo=0
num_co=0
_string = input("Enter your string: ")
for i in _string.strip():
    if i in ['a','e','i','o','u']:
        print(f"{i} is a vowel")
        num_vo+=1
    else:
        print(f"{i} is a consonant")
        num_co+=1
print(f"vowel is: {num_vo}")
print(f"consonant is: {num_co}")

