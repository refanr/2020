def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    # ... and the rest is up to you
    updated_sequence = ''
    for i in range(len(sequence)):
        if i != index_to_remove:
            updated_sequence += sequence[i]
        
    return updated_sequence,  sequence[index_to_remove]

