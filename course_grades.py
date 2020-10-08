# Biður notanda um skráarnöfn fyrir 'parts' og 'grades'
# Opna parts skrá og prenta út lista af túplum
# Opna grades skrá og prenta út lista af túplum
# Taka gögn úr báðum listum og reikna út vegna lokaeinkunn og bæta henni í lista 2
# Upplýsingar teknar og prentaðar út á skýran hátt

# Functions here

def get_filename(initial):
    which = ''
    if initial == 'g':
        which = 'grades'
    elif initial == 'p':
        which = 'parts'

    filename = input('Enter filename for {}: '.format(which))

    return filename

def make_a_list(filename):
    parts_list = []
    temp_list = []
    try:
        file_object = open(filename, 'r')
    except FileNotFoundError:
        print('File {} not found'.format(filename))
    for line in file_object:
        temp_list.append(line.split())
    
    for i in range(len(temp_list[0])):
        tup = (temp_list[0][i], float(temp_list[1][i]))
        parts_list.append(tup)
        
    return parts_list




def calc_final(parts, grades):
    return 'wow'

def print_all_nice_and_tidy(final_grades):
    print('wowie')

# Main program starts here
part_file = get_filename('p')
parts = make_a_list(part_file)
print(parts)

grades_file = get_filename('g')
grades = make_a_list(grades_file)
print(grades)

final_grades = calc_final(parts, grades)

print(final_grades)
print_all_nice_and_tidy(final_grades)


