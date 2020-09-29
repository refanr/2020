# ...add your functions
def open_file(filename):
    file_obj = open(filename, "r")
    return file_obj

def print_lines(file_obj1, file_obj2):
    out = ''
    for line in file_obj1:
        out += line
        
    
# You can keep these lines
file_name_a = input("First file: ")
file_name_b = input("Second file: ")
file_object_1 = open_file(file_name_a)
file_object_2 = open_file(file_name_b)

print_lines(file_object_1,file_object_2)

# ...fill in the rest