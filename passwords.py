password = input('Enter a new password: ')
Min_length = 6
Max_length = 20
lower_check = False
upper_check = False
num_check = False


passwords = 0
valid_pass = 0
invalid_pass = 0

while password != 'q':
    if Min_length <= len(password) <= Max_length:
        for char in password:
            if char.islower():
                lower_check = True
            elif char.isupper():
                upper_check = True
            elif char.isnumeric:
                num_check = True
        else:
            if lower_check == False:
                invalid_pass += 1
                print('At least one lower case letter needed')
                if upper_check == False:
                    print('At least one upper case letter needed')
                elif num_check == False:
                    print('At least one number needed')
            elif upper_check == False:
                invalid_pass += 1
                print('At least one upper case letter needed')
                if num_check == False:
                    print('At least one number needed')
            elif num_check == False:
                invalid_pass += 1
                print('At least one number needed')
            elif lower_check and upper_check and num_check:
                valid_pass += 1
                print('Valid password of length', len(password))
            else:
                invalid_pass += 1    
    else:
        print('Invalid length')
        invalid_pass += 1

    lower_check, upper_check, num_check = False, False, False
    passwords += 1
    password = input('Enter a new password: ')

print('You tried ' + str(passwords) + ' passwords, {} valid, {} invalid'.format(str(valid_pass),str(invalid_pass)))