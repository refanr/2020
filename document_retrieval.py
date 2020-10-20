import string

def get_filename():
    filename = input('Document collection: ')

    return filename

def open_doc_collection(filename):
    try:
        file_obj = open(filename, 'r')
    except FileNotFoundError:
        print('Documents not found.')

    return file_obj

def get_documents(file_object):
    doc_list = []
    for line in file_object:
        tmp_str = ''
        tmp_list = line.split()
        for word in tmp_list:
            tmp_str = tmp_str + word
        else:
            tmp_str = tmp_str + '/n'
        doc_list.append(tmp_str)
    print(doc_list)


    

def get_print_docs(printable_docs):
    pass
            


def dictionarize(docs_list):
    pass
    

def show_menu():
    print('\nWhat would you like to do?')
    print('1. Search Documents')
    print('2. Print Document')
    print('3. Quit Program')

def search_docs(docs_dict):
    pass
        

def print_doc(docs_list, new_printable_docs):
    pass

def get_choice():
    return input('> ')

def main():
    file_object = open_doc_collection(get_filename())
    docs_list, printable_docs = get_documents(file_object)
    new_printable_docs = get_print_docs(printable_docs)
    docs_dict = dictionarize(docs_list)
    show_menu()
    choice = get_choice()
    while_bool = True
    while while_bool:
        if choice == '1':
            search_docs(docs_dict)
            show_menu()
            choice = get_choice()
        elif choice == '2':
            print_doc(docs_list, new_printable_docs)
            show_menu()
            choice = get_choice()
        else:
            while_bool = False
    print('Exiting program.')   

main()