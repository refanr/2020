# Taking in the length of the sequence from the user
# Seqence goes as follows:
# Starting from 1, 2 and 3, the code will add the current number
# to the sum of the previous 2 numbers.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_int = 1
second_int = 2
print(first_int)
print(second_int)
current_int = 3

for i in range(1, n-1):
    print(current_int)
    current_int = current_int + first_int + second_int
    
    first_int, second_int = second_int, (current_int - first_int - second_int)
    
    
    
