# You might need this to calculate a square root using math.sqrt
import math
number = int(input('Enter a number (-1 to exit) '))
current_average = number
standard_deviation = 0.0
num_sum = 0

difference = 0
difference_sum = 0
count = 1
# Loop until the user types in -1
while number != -1:
    num_sum += number
    current_average = (num_sum) / (count)

    difference = number - current_average
    squared = difference ** 2
    difference_sum += squared

    if count > 1:
        standard_deviation = math.sqrt(difference_sum/(count-1))    

    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))
    count += 1
    number = int(input('Enter a number (-1 to exit) '))
