# Biðja um skráarnafn og ath hvort það finnst
# Opna skrá og gera lista úr hverri línu fyrir sig
# Taka listann og prenta út fyrstu tvo listana í aðallistanum

def get_filename():
    file_name = input('Enter file name: ')
    return file_name

def open_file(filename):
    try:
        file_object = open(file_name,'r')
    except FileNotFoundError:
        print('File {} not found'.format(file_name))

    return file_object

def process_names(file_object):
    name_list = []
    for line in file_object:
        line_list = line.split()
        output_list = []
        for item in line_list:
            try:
                item = int(item)
                output_list.append(item)
            except ValueError:
                output_list.append(item)
        name_list.append(output_list)
    
    return name_list

def print_lists(namelists):
    print_list = namelists[0:2]
    print(print_list)

# Main program starts here
file_name = get_filename()

file_object = open_file(file_name)

namelists = process_names(file_object)

print_lists(namelists)
