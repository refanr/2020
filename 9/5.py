# Main program starts here
filename = input("Enter filename: ")

file_object = open(filename, "r")

for line in file_object:
    out = line.replace(' ', '\n').strip()
    print(out)