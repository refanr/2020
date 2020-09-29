import string

# Implement a function here
def uniqueify(sentence):
    unique = []
    uni = ''
    for char in sentence:
        check = string.ascii_letters
        if char in check:
            if char in uni:
                pass
            else:
                uni += char
    unique.extend(uni)

    return unique
            
       

# Main starts here
sentence = input("Input a sentence: ")
# Call the function here
unique_letters = uniqueify(sentence)
print("Unique letters:", unique_letters)
