def menu_selection():
    print('Menu:')
    choice = input('(a)dd, (r)emove, (f)ind: ')
    return choice

def add_to_dict(a_dict):
    key = input('Key: ')
    val = input('Value: ')
    if key in a_dict:
        key_error('a')
    else:
        a_dict[key] = val

def key_error(type):
    if type == 'a':
        print('Error. Key already exists.')
    else:
        print('Key not found.')

def remove_from_dict(a_dict):
    key = input('Key to remove: ')
    if key in a_dict:
        a_dict.popitem(key)
    else:
        key_error('r')
    
def find_key(a_dict):
    key = input('Key to locate: ')
    if key in a_dict:
        print('Value: {}'.format(a_dict[key]))
    else:
        key_error('f')

        

def execute_selection(choice, a_dict):
    if choice == 'a':
        add_to_dict(a_dict)
    elif choice == 'r':
        remove_from_dict(a_dict)
    elif choice == 'f':
        find_key(a_dict)
    else:
        print('Invalid choice.')

def dict_to_tuples(a_dict):
    tuple_list = []
    for key in a_dict:
        tmp = (key, a_dict[key])
        tuple_list.append(tmp)
    return tuple_list

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()