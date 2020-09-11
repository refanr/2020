dog_age = int(input("Input dog's age: ")) # Do not change this line
one_yo_dog = 15
two_yo_dog = 24

if 1 <= dog_age <= 16:
    if dog_age == 1:
        print('Human age:', one_yo_dog)
    elif dog_age == 2:
        print('Human age:', two_yo_dog)
    else:
        print('Human age:', two_yo_dog + (4 * (dog_age-2)))
        
else:
    print('Invalid age')