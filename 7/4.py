# is_prime function definition goes here
def is_prime(param):
    prime = True
    for i in range(2,param):
        if param == 2:
            prime = True
        elif param % i == 0:
            prime = False
            break
        else:
            prime = True
    return prime   
    

    
max_num = int(input("Input an integer greater than 1: "))

# Call the function here repeatadly from 2 to max_num and print out the appropriate message
for i in range(2,max_num+1):
    if is_prime(i) == True:
        print(i, "is a prime")
    else:
        print(i, "is not a prime")
