
# is_float function definition goes here
def is_float(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False

# Example usage
print(is_float('3.45'))
print(is_float('abc'))
