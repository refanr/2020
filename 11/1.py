#list_to_int_tuple function goes here
def list_to_int_tuple(listi):
    temp_list = []
    for i in listi:
        try:
            temp_list.append(int(i)) 
        except ValueError:
            pass
    return tuple(temp_list)


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)