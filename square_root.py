import math

start_int = int(input("Input starting integer: "))

while start_int >= 2:
    start_int = math.sqrt(start_int)
    print(round(start_int,4))
    