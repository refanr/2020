def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    # ... and the rest is up to you
    if occurrence == 1:
        return sequence.find(element_to_find)
    elif occurrence == 3:
        return sequence.rfind(element_to_find)
    elif occurrence == 2:
        split_string = sequence.split(sep='|')
        return len(split_string[0]) + len(split_string[1]) + 1
    else:
        return -1


