def name_number():
    name = input('Name: ')
    number = input('Number: ')
    data_dict[name] = number

def make_a_list(data_dict):
    out = []
    for key in data_dict:
        tmp = (key, data_dict[key])
        out.append(tmp)
    return out

more_data = 'y'
data_dict = {}

while more_data == 'y':
    name_number()
    more_data = input('More data (y/n)? ')

out = []
for key in data_dict:
        tmp = (key, data_dict[key])
        out.append(tmp)
out.sort()
print(out)

    
