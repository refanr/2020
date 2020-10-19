def get_name():
    return input('Enter name: ').strip().lower().split()

def character_lst(name):
    char_lst = []
    first = name[0]
    second = name[1]
    for char in first:
        if char in second:
            if char not in char_lst:
                char_lst.append(char)
    return char_lst

def character_set(name):
    char_set = set()
    first = name[0]
    second = name[1]
    for char in first:
        if char in second:
            char_set.add(char)
    return char_set


# Main program starts here

name = get_name()
print(sorted(character_lst(name)))
print(sorted(character_set(name)))