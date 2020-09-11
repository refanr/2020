a_str = input("Input a float: ")

a_str = round(float(a_str), 2)
a_str = str(a_str)
if a_str[-1] == '0':
    a_str = a_str + '0'



print(a_str.rjust(12))