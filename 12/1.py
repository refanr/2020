def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def check_list(int_list):
    bool_c = True
    for i in int_list:
        try:
            int(i)
        except ValueError:
            print('Error: enter only integers.')
            bool_c = False
    return bool_c

def sorted_list(int_list):
    int_list.sort()
    print('Sorted list:',int_list)

def prime_list(int_list):
    new_list = []
    for i in range(0,len(int_list)):
        if is_prime(int_list[i]):
            if int_list[i] not in new_list:
                new_list.append(int_list[i])
    print('Prime list: ', new_list)

def min_max(int_list):
    summ, length = int(sum(int_list)), len(int_list)
    avg = round(summ/length,2)
    print('Min: {}, Max: {}, Average: {}'.format(min(int_list), max(int_list), avg))
        
# The main program starts here
int_inp = input('Enter integers separated with commas: ')
int_list = int_inp.split(',')
checked = check_list(int_list)

if checked == True:
    int_list = [int(i) for i in int_list]
    print('Input list:',int_list)
    sorted_list(int_list)
    prime_list(int_list)
    min_max(int_list)

