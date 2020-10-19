import string

def get_word_list(file_object):
    word_list = []
    for line in file_object:
        ind_words = line.split()
        for word in ind_words:
            word = word.strip()
            word = word.strip('.,?!')

            word_list.append(word.lower())
        
            
    
    return word_list

def word_list_to_counts(word_list):
    word_count_dict = {}
    for item in word_list:
        if item in word_count_dict:
            word_count_dict[item] += 1
        else:
            word_count_dict[item] = 1
    
    return word_count_dict        

def dict_to_tuples(word_count_dict):
    word_count_tuples = []
    for key in word_count_dict:
        tmp = (key, word_count_dict[key])
        word_count_tuples.append(tmp)
    
    return word_count_tuples

def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    
main()