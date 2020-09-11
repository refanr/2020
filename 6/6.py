name = input("Input a name: ")
split_name = name.split()

last_name = str(split_name[0]).capitalize()


first_name = str(split_name[-1]).capitalize()

print(first_name[0] + ". " + last_name[:-1])

