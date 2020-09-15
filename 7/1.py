# The function definition goes here
def every_other(chop_string):
    """Takes an input and  returns every other character"""
    result = ''
    for i in range(len(chop_string)):
        if i == 0:
            result += chop_string[i]
        elif i % 2 == 0:
            result += chop_string[i]
    return result


input_str = input("Enter a string: ")

# You call the function here
outp = every_other(input_str)
print('Every other character: ' + outp)