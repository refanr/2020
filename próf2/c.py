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

def print_lists(namelists,boys_list,girls_list):
    print(namelists[0:2])
    print(boys_list[0:5])
    print(girls_list[0:5])
    boy_frequency, girl_frequency = get_frequency(boys_list, girls_list)
    percentile_50_boys, percentile_50_girls = get_50th(boys_list, girls_list)
    print('Total frequency of boy names:',boy_frequency)
    print('Total frequency of girl names:',girl_frequency)
    print('50th percentile rank for boys:',percentile_50_boys)
    print('50th percentile rank for girls:',percentile_50_girls)
    
def seperate_lists(namelists):
    boys_list, girls_list = [], []
    out_boys, out_girls = [], []
    for lst in namelists:
        boys_list.append(lst[1])
        boys_list.append(lst[2])
        girls_list.append(lst[3])
        girls_list.append(lst[4])
        out_boys.append(boys_list[:])
        out_girls.append(girls_list[:])
        boys_list.clear()
        girls_list.clear()        
    
    return out_boys, out_girls

def get_frequency(boys_list, girls_list):
    boy_frequency, girl_frequency = 0, 0
    for lst in boys_list:
        boy_frequency += lst[1]

    for lst in girls_list:
        girl_frequency += lst[1]

    return boy_frequency, girl_frequency



# Main program starts here
file_name = get_filename()
file_object = open_file(file_name)
namelists = process_names(file_object)
boys_list, girls_list = seperate_lists(namelists)


print_lists(namelists,boys_list,girls_list)
