# max_of_three function definition goes here
def max_of_three(first, second, third):
    return max(first,second,third)


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Call the function here
maximum = max_of_three(third,second,first)

print("Maximum:", maximum)