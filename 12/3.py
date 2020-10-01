import string

def get_words(file_name):
    file_obj = open(file_name, 'r')
    listi = []
    for line in file_obj:
        temp_list = line.split()
        for l in temp_list:
            listi.append(l)
    new_list =[]


    for word in listi:
        clean_word = str(word)
        
        new_list.append(clean_word.strip(string.punctuation))
    return new_list

def remove_dups(list_of_words):
    new_list = []
    for i in list_of_words:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list
        
        

file_name = input('Enter a filename: ')

list_of_words = get_words(file_name)
single_words = remove_dups(list_of_words)
print(single_words)
