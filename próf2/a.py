# Birta valmynd
# Taka við vali notanda
# Taka við tölunum frá notanda
# Beina tölum í rétt fall, sum og margfeldi
# Prenta út niðurstöðu
# Birta valmynd aftur og aftur þangað til notandi velur 9

def show_menu():
    
    print('1: Compute the sum of 1..n')
    print('2: Compute the product of 1..n')
    print('9: Quit')
    
    choice = get_choice()
    return choice

def get_choice():
    choice = input('Choice: ')
    return choice    

def sum_compute():
    sum_result = 0
    try:
        n_value = int(input('Enter value for n: '))
        
        for i in range(n_value+1):
            sum_result += i

        print('The result is:', sum_result)
    except ValueError:
        pass

def product_compute():
    product_result = 1
    try:
        n_product_value = int(input('Enter value for n: '))
        
        for i in range(1,n_product_value+1):
            product_result *= i
        print('The result is:', product_result)

    except ValueError:
        pass

# Main program starts here

choice = show_menu()

while choice != '9':
    
    if choice == '1':
        sum_compute()
    elif choice == '2':
        product_compute()

    choice = show_menu()
    