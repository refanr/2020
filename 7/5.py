# palindrome function definition goes here
def is_pal(param):
    working = ''
    for char in param:
        if char.isalpha():
            working += char.lower()
    
    if working == working[::-1]:
        return True   


in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if is_pal(in_str) == True:
    print('"' + in_str + '"' + ' is a palindrome.')
else:
    print('"' + in_str + '"' + ' is not a palindrome.')