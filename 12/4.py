def check_list(int_list):
    bool_c = True
    for i in int_list:
        try:
            int(i)
        except ValueError:
            print('Error: enter only integers.')
            return False
    check_cons(int_list)

def check_cons(int_list):
    check_int = int(input('Consecutive check: '))
    bool_c = False
    for i in range(0,len(int_list)):
        if check_int == int(int_list[i]):

            if int_list[i]==int_list[i-1]:
                bool_c = True
    print(bool_c)    
    
            
    

int_input = input('Enter elements of list separated by commas: ')
int_list = int_input.split(',')
check_list(int_list)

