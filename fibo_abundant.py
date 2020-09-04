choice = input('Input f|a|b (fibonacci, abundant or both): ')

if choice == 'f' or choice == 'b':
    #Fibonacci sequence
    length = int(input('Input the length of the sequence: '))
    print('Fibonacci sequence:')
    print('-------------------')
    first_no = 0
    second_no = 1
    print(first_no)
    print(second_no)
    current_no = 0

    for i in range(1,length-1):
        current_no = first_no + second_no
        print(current_no)

        first_no, second_no = second_no, current_no

    

if choice == 'a' or choice == 'b':
    #Abundant numbers
    max_num = int(input('Input the max number to check: '))
    print('Abundant numbers: ')
    print('-----------------')
    proper_divisor_sum = 0

        
    for i in range(1,max_num+1):
        proper_divisor_sum = 0
        for j in range(1,i):
            if i % j == 0:
                proper_divisor_sum += j
                if i < proper_divisor_sum:
                    print(i)
                    break
            else:
                continue

            