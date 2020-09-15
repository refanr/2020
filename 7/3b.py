def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    # ... and the rest is up to
    updated_sequence = ''
    for i in range(len(sequence)+1):
        if i < index:
            updated_sequence += sequence[i]
        elif i == index:
            updated_sequence += element
        elif i > index:
            updated_sequence += sequence[i-1]

    return updated_sequence

