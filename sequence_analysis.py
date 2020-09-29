# Take in file names
# For each file, open it and read it
# Check if each number is actually a number and then put it in a sequence
# Make a sorted sequence and an ordered sequence
# Take the ordered sequence and find the median value
# Finally print the results

def process_all_files(filename_list):
    for file in filename_list:
        try:
            file_obj = open(file, "r")
            print('\nFile', file)
            read_from_file(file_obj)
            file_obj.close()
            
        except FileNotFoundError:
            print('\nFile', file, 'not found')

def read_from_file(file_obj):
    sequence = []
    working_number = 0.0
    for line in file_obj:
        try:
            working_number = float(line.strip())
            sequence.append(working_number)
        except ValueError:
            pass
        
    process_sequences(sequence)

def process_sequences(sequence):
    cumulative_sequence = []
    sorted_sequence = []
    sorted_sequence += sequence
    working_number = 0.0
    for num in sequence:
        working_number += float(num)
        cumulative_sequence.append(round(working_number,1))
    
    sorted_sequence.sort()
    median = find_median(sorted_sequence)
    stringify_all(sequence, cumulative_sequence, sorted_sequence, median)

def stringify_all(sequence, cumulative_sequence, sorted_sequence, median):
    sequen = ''
    cumulative = ''
    sorted = ''
    for i in range(0,len(sequence)):
        sequen = sequen + ' ' + str(sequence[i])
        cumulative = cumulative + ' ' + str(cumulative_sequence[i])
        sorted = sorted + ' ' + str(sorted_sequence[i])
    print_all(sequen, cumulative, sorted, median)

def find_median(sequence):
    length = len(sequence)
    median = 0.0
    index = length // 2
    try:
        if length % 2 == 0:
            median = (sequence[index-1] + sequence[index]) / 2
        else:
            median = sequence[index]
    except IndexError:
        pass
    return round(median,2)

def print_all(sequence, cumulative_sequence, sorted_seq, median):
    if len(sequence) != 0:
        sequence, cumulative_sequence, sorted_seq = sequence.strip() + ' ', cumulative_sequence.strip() + ' ', sorted_seq.strip() + ' '
    else:
        sequence, cumulative_sequence, sorted_seq = sequence.strip(), cumulative_sequence.strip(), sorted_seq.strip()
    
    print("\tSequence:\n\t\t" + sequence)
    print("\tCumulative sum:\n\t\t" + cumulative_sequence)
    print("\tSorted sequence:\n\t\t" + sorted_seq)
    print("\tMedian:")
    if median != 0.0:
        print("\t\t" + str(median).strip())
    else:
        print("\t\t")

# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
