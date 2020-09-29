def get_emails():
    email = ''
    email_list = []
    while email != 'q':
        email = input('Email address: ')
        if email != 'q':
            email_list.append(email)
    return email_list


def get_names_and_domains(listi):
    tuple_list = []
    for i in listi:
        tup = tuple(i.split('@'))
        tuple_list.append(tup)
    return tuple_list

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)