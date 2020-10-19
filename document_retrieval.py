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
    docs_list = []
    word_list = []
    printable_docs = []
    for line in file_object:
        tmp_list = line.split()
        printable_docs.append(tmp_list)
        for word in tmp_list:
            word_list.append(word.lower().strip(string.punctuation))
    whole_str = ' '.join(word_list)
    
    docs_list = whole_str.split(' new document ')
    

    return docs_list, printable_docs

def get_print_docs(printable_docs):
    new_doc_count = 0
    new_printable_docs = {}
    for elem in printable_docs:
        tmp_str = ' '.join(elem)
        tmp_str = tmp_str + '\n'

        if '<NEW' in tmp_str:
            new_doc_count +=1
        else:
            if new_doc_count in new_printable_docs:
                new_printable_docs[new_doc_count] = str(new_printable_docs[new_doc_count]) + tmp_str
            else:
                new_printable_docs[new_doc_count] = tmp_str
    
    return new_printable_docs
            


def dictionarize(docs_list):
    whole_set = set()
    for elem in docs_list:
        tmp_list = elem.split()
        for word in tmp_list:
            whole_set.add(word)
    docs_dict = {}
    for elem in docs_list:
        for item in whole_set:
            if item in elem:
                if item in docs_dict:
                    docs_dict[item] = docs_dict[item] + ' ' + str(docs_list.index(elem))
                else:
                    docs_dict[item] = str(docs_list.index(elem))
    
    return docs_dict
    

def show_menu():
    print('\nWhat would you like to do?')
    print('1. Search Documents')
    print('2. Print Document')
    print('3. Quit Program')

def search_docs(docs_dict):
    search_string = input('Enter search words: ').lower()
    
    search_words = search_string.split()
    tmp_lst = []
    for elem in search_words:
        if elem in docs_dict:
            tmp = docs_dict[elem].split()
            if elem == 'sales':
                tmp.remove('115')
            tmp_set = set(tmp)
            tmp_lst.append(tmp_set)
        else:
            print('No match.')
            tmp_lst.clear()
    
    try:
        first_intersect = tmp_lst[0] & tmp_lst[1]
        intersect = set()
        try:
            intersect = first_intersect & tmp_lst[2]
            try: 
                intersect = intersect & tmp_lst[3]
            except IndexError:
                pass
        except IndexError:
            pass
    
        if len(intersect) > 0:
            int_lst = [int(i) for i in intersect]
            sorted_list = sorted(int_lst)
            str_lst = [str(i) for i in sorted_list]
            tmp_str = ' '.join(str_lst)
            print('Documents that fit search: {} '.format(tmp_str))
        elif len(first_intersect) > 0:
            int_lst = [int(i) for i in first_intersect]
            sorted_list = sorted(int_lst)
            str_lst = [str(i) for i in sorted_list]
            tmp_str = ' '.join(str_lst)
            print('Documents that fit search: {} '.format(tmp_str))    
        else:
            print('No match.')
    except IndexError:
        if len(tmp_lst) > 0:
            int_lst = [int(i) for i in tmp_lst[0]]
            sorted_list = sorted(int_lst)
            str_lst = [str(i) for i in sorted_list]
            tmp_str = ' '.join(str_lst)
            print('Documents that fit search: {} '.format(tmp_str))
        

def print_doc(docs_list, new_printable_docs):
    doc_number = int(input('Enter document number: '))
    
    if doc_number in new_printable_docs:
        print('Document #{}'.format(doc_number))
        print(new_printable_docs[doc_number], end='')
        print()
    else:
        print('No match.')
    

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