# Biður notanda um skráarnöfn fyrir 'parts' og 'grades'
# Opna parts skrá og prenta út lista af túplum
# Opna grades skrá og prenta út lista af túplum
# Taka gögn úr báðum listum og reikna út vegna lokaeinkunn og bæta henni í lista 2
# Upplýsingar teknar og prentaðar út á skýran hátt

# Functions here

def get_filename(initial):
    ''' Takes in a filename from the user '''
    which = ''
    if initial == 'g':
        which = 'grades'
    elif initial == 'p':
        which = 'parts'

    filename = input('Enter filename for {}: '.format(which))

    return filename

def make_a_list_parts(filename):
    ''' Makes a list of parts, formatted to specs '''
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
    file_object.close()

    return parts_list

def make_a_list_grades(filename):
    ''' Makes a list of grades, formatted to specs '''
    grades_list = []
    temp_list = []
    try:
        file_object = open(filename, 'r')
    except FileNotFoundError:
        print('File {} not found'.format(filename))
    for line in file_object:
        temp_list = line.split()
        user = temp_list[0]
        temp_list.pop(0)
        tmp_list = [float(i) for i in temp_list]
        tup = (user, tmp_list)
        grades_list.append(tup)
    file_object.close()

    return grades_list

def calc_final(parts, grades):
    ''' Calculates weighted final grade for each student '''
    updated_grades =[]
    for elem in grades:
        temp_sum = 0.0
        for i in range(len(parts)):
            multiplier = parts[i][1]
            grade_to_calc = elem[1][i]
            temp_sum += grade_to_calc * multiplier
        tup = (elem[0], elem[1], temp_sum)
        updated_grades.append(tup)
    
    return updated_grades


def print_all_nice_and_tidy(final_grades):
    ''' Prints results, according to specs '''
    print('\n{:>16s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}'.format('Student ID','Quizzes','Assignments', 'Projects','Midterms','Final', 'Course grade'))
    for elem in final_grades:
        final = elem[2]
        f = str(round(final,2))
            
        print('{:>16s}{:>14.1f}{:>14.1f}{:>14.1f}{:>14.1f}{:>14.1f}{:>14s}'.format(elem[0],elem[1][0],elem[1][1],elem[1][2],elem[1][3],elem[1][4],f))

# Main program starts here
part_file = get_filename('p')
parts = make_a_list_parts(part_file)
print(parts)

grades_file = get_filename('g')
grades = make_a_list_grades(grades_file)
print(grades)

final_grades = calc_final(parts, grades)

print(final_grades)
print_all_nice_and_tidy(final_grades)


