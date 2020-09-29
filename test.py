temp = open('b.txt', 'r')

for line in temp:
    tmp = line.strip()
    try:
        tmp = float(line)
        print(tmp)
    except ValueError:
        pass
        