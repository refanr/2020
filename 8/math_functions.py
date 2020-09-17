#   Define the functions: sum_natural, sum_fibonacci and approximate_euler
#   Define a menu function for the user to choose from, repeatedly, until he selects the x, exit option
import math

def menu():
    print('Please choose one of the options below:')
    print('a. Display the sum of the first N natural numbers.')
    print('b. Display the sum of the first N Fibonacci numbers.')
    print('c. Display the approximate value of e using N terms.')
    print('x. Exit from the program.')
    print()


def sum_natural(n_str):
    sum = 0
    num = int(n_str)

    if num >= 2:
        for i in range(num+1):
            sum += i
    else:
        return None
    
    print('Natural number sum:',sum)


def sum_fibonacci(n_str):
    sum = 0
    num = int(n_str)
    first_num = 0
    second_num = 1
    current_num = 0

    if num >= 2:
        for i in range(1,num+1):
            sum += first_num
            current_num = first_num + second_num
            first_num, second_num = second_num, current_num        
    else:
        return None
    print('Fibonacci sum:',sum)


def approximate_euler(n_str):
    approximation = 2
    num = int(n_str)

    if num >= 2:
        for i in range(2,num):
            approximation += 1/(math.factorial(i))
        
    else:
        return None

    print('Euler approximation:',round(approximation,5))

menu()
option = ''
chosen_n = ''

while option != 'x':
    option = input('Enter option: ')
    if option == 'a' or option == 'b' or option == 'c':
        chosen_n = input('Enter N: ')
        if chosen_n.isnumeric() == False:
            print('Error: ' + chosen_n + ' was not a valid number.')
            continue
        elif int(chosen_n) < 2:
            print('Error: ' + chosen_n + ' was not a valid number.')
            continue

        if option == 'a':
            sum_natural(chosen_n)
        elif option == 'b':
            sum_fibonacci(chosen_n)
        elif option == 'c':
            approximate_euler(chosen_n)
    else:
        print('Unrecognized option ' + option)
        menu()
