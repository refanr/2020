# Your functions should appear here


def append_words():
    word_list = []
    while True:
        word = input('Enter word to be added to list: ')
        if word == 'x':
            break
        else:
            word_list.append(word.strip())
    return word_list
    
def check_words(arglist):
    newlist = []
    for elem in arglist:
        if len(elem) > 1:
            if elem[0] == elem[-1]:
                newlist.append(elem)
    return newlist


# Main program starts here
# It should mostly be a sequence of function calls

appended = append_words()
nl = check_words(appended)
new_str = '\n'.join(nl)

print(appended)
print(new_str)


