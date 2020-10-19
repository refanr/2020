def get_set():
    a_list = input('Input a list of integers separated with a comma: ').strip().split(',')
    a_list = [int(i) for i in a_list]
    return set(a_list)

def get_menu():
    print('1. Intersection')
    print('2. Union')
    print('3. Difference')
    print('4. Quit')

def main():
    set_a = get_set()
    set_b = get_set()
    print(set_a)
    print(set_b)
    selection = ''
    while selection != '4':
        get_menu()
        selection = input('Set operation: ')
        if selection == '1':
            print(set_a & set_b)
        elif selection == '2':
            print(set_a | set_b)
        elif selection == '3':
            print(set_a - set_b)
# Main program
main()
