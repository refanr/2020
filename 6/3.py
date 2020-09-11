a_str = input("Input a string: ")
lower_int = 0
upper_int = 0
for char in a_str:
    if char.islower() == True:
        lower_int += 1
    elif char.isupper() == True:
        upper_int += 1
print(lower_int)
print(upper_int)
 