# Your functions here
def open_file(filename):
    file_object = open(filename, "r")
    return file_object


def find_longest(file_object):
    longest_word = ''
    for line in file_object:
        if len(line.strip()) > len(longest_word):
            longest_word = line.strip()
    return longest_word

# Main program starts here
try:
    filename = input("Enter filename: ")

    file_object = open_file(filename)
    if file_object:
        longest_word = find_longest(file_object)
        print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
        file_object.close()
    else:
        print("File not found")
except FileNotFoundError:
    print("File not found")