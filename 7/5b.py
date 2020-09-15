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


def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    updated_sequence = ''
    for i in range(len(sequence)):
        if i != index_to_remove:
            updated_sequence += sequence[i]
        
    return updated_sequence,  sequence[index_to_remove]


def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    updated_sequence = ''
    for i in range(len(sequence)+1):
        if i < index:
            updated_sequence += sequence[i]
        elif i == index:
            updated_sequence += element
        elif i > index:
            updated_sequence += sequence[i-1]

    return updated_sequence


def move_one(from_pillar, to_pillar, state):
    """ Moves the topmost disc from one pillar to another and returns the updated state representation. """
    # ... implement this method, utilizing the functions defined above
    top_number = find_index_of_nth_occurrence(state, '|', from_pillar) -1
    state, char = remove_at(state, top_number)

    next_number = find_index_of_nth_occurrence(state, '|', to_pillar)
    state = insert_at(state, next_number, char)

    return state
# ... add your functions from the previous solution here at the top

def move_many(how_many, from_pillar, to_pillar, state):
    """ Moves the specified number of discs from one pillar to another and returns the updated state representation. 
    
    Prints the state for every move made.
    """
    # ... implement this method
    while how_many > 0:
        state = move_one(1,3,state)
        print(state)
        how_many = find_index_of_nth_occurrence(state,'|',1)
        


# Keep the following lines as they are
number_of_discs = int(input("How many discs are on the left-most pillar? "))
initial_state = ""
for disc in range(number_of_discs, 0, -1):
    initial_state += str(disc)
initial_state += "|||"
print(initial_state)
move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)
