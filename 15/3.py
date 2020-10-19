import string
from operator import itemgetter

def get_filename():
    return input('Enter name of file: ')

def open_file(filename):
    try:
        file_object = open(filename, 'r')
    except FileNotFoundError:
        print('File {} not found.'.format(filename))
    return file_object

def get_bigrams(file_object):
    word_list = []
    bigrams = []
    for line in file_object:
        tmp_list = line.split()
        for word in tmp_list:
            word_list.append(word.strip(string.punctuation).lower())

    for i in range(len(word_list)):
        try:
            tup = (word_list[i], word_list[i+1])
            bigrams.append(tup)
        except IndexError:
            pass

    return bigrams
    
def count_bigrams(bigrams):
    bigram_dict = {}
    for elem in bigrams:
        if elem in bigram_dict:
            bigram_dict[elem] += 1
        else:
            bigram_dict[elem] = 1

    bigram_lst = bigram_dict.items()
    
    return sorted(bigram_lst,key=itemgetter(1),reverse=True)

def main():
    filename = get_filename()
    file_object = open_file(filename)
    bigrams = get_bigrams(file_object)
    print(count_bigrams(sorted(bigrams))[:9])

main()