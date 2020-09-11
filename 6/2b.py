email_address = input("Email address: ")
print("Checking...")
spaces = ' '

# ...and the rest is up to you
if email_address.find('@') == -1:
    print('@ symbol is missing')
elif email_address.find('@') != email_address.rfind('@'):
    print(email_address)
    spaces = ' ' * email_address.rfind('@')
    print(spaces + "^--there's an extra @ symbol here")
elif email_address[0] == '@':
    print(spaces + email_address)
    print("^--this bit is missing")
elif email_address[-1] == '@':
    print(email_address)
    spaces = ' ' * len(email_address)
    print(spaces + "^--this bit is missing")
    spaces = ' '
elif email_address[0] == '.':
    print(email_address)
    print("^--there's a dot here that probably shouldn't")
elif email_address[email_address.find('@')-1] == '.':
    print(email_address)
    spaces = ' ' * (email_address.find('@') - 1)
    print("^--there's a dot here that probably shouldn't")
elif email_address[email_address.find('.') + 1] =='.':
    print(email_address)
    spaces = ' ' * email_address.find('.')
    print("^--there are consecutive dots here")
elif email_address.find('.', email_address.find('@')) == -1:
    print("The top-level-domain is missing. Did you perhaps intend to write " + email_address + ".com?")
else:
    print('Seems legit')