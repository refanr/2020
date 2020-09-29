# Main starts here
file_name = input("Enter filename: ")

temp_file = open(file_name, "r")
text = ''

for line in temp_file:
    text += line.replace(' ','').strip()

print(text)
    