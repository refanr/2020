my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
working_int = my_int
quotient = 1
bin_str = ''

while quotient > 0:
    if working_int % 2:
        bin_str += '1'
    else:
        bin_str += '0'
    
    quotient = working_int // 2
    
    working_int = quotient

bin_str = bin_str[::-1]

print("The binary of {} is {}".format(my_int,bin_str))