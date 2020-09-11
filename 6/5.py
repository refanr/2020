a_str = input("Input a string: ")
letters_int = 0 
words_int = 0

for char in a_str:
    if char == ' ':
        words_int += 1
        
    elif char.isalpha:
        if char == ',' or char == '.':
            continue
        else:
            letters_int += 1
    
else:
    words_int += 1


print('No. of letters: {}, no. of words: {}'.format(letters_int, words_int))