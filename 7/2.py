# Your function definition goes here
def count_digits(param):
    result = 0
    for char in param:
        if char.isdigit() == True:
            result += 1

    return result

input_str = input("Enter a string: ")

# Call the function here
digit_count = count_digits(input_str)

print("No. of digits:", digit_count)