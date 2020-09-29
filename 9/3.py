def divide_safe(num1, num2):
    try:
        return round(float(num1) / float(num2),5)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

num1_str = input('Input first number: ')
num2_str = input('Input second number: ')

result = divide_safe(num1_str, num2_str)
print(result)