# 1. Taka inn location og átt sem bátarnir snúa
# 2. Ath hvort báturinn fer út fyrir leikborðið, senda villuboð og endurtaka spurninguna, annars búa til coordinates fyrir hann
# 3. Spyrja um coordinates fyrir árás
# 4. Athuga hvort og þá hvað skotið hittir og tilkynna hvort er
# 5. Uppfæra fleet fyrir while lúppuna


SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)

 
# ... add your functions here
def gather_fleet_positions():
    print("Specify the location of each ship in your fleet by providing the top/left coordinate and orientation.")
    print("Examples: 'A2 vertical' or 'C3 horizontal'")
    fleet = []
    carrier,battleship,destroyer,submarine,patrol = carrier_pos(),battleship_pos(),destroyer_pos(),submarine_pos(),patrol_pos()

    
def carrier_pos():
    size = 5
    location = input('Location and orientation of your carrier: ')
    coordinate = location.split()
    orientation = coordinate[1]
    cor_x, cor_y = coordinate[0].split()
    cor_x = int(cor_x)
    x_vals = [cor_x]
    y_vals = [cor_y]
    if orientation == 'horizontal':
        if (cor_x + size) > 10:
            print('Ship to big for this location, try again.')
            carrier_pos()
        else:
            for i in range(size):
                x_vals.append(cor_x + 1)
    else:
        if cor_y.lower() not in 'abcdef':
            print('Ship to big for this location, try again.')
            carrier_pos()
        else:
            

        
def battleship_pos():
    size = 4
    location = input('Location and orientation of your battleship: ')
    coordinate = location.split()
    orientation = coordinate[1]
    cor_x, cor_y = coordinate[0].split()
    x_vals = [cor_x]
    if orientation == 'horizontal':
        if (cor_x + size) > 10:
            print('Ship to big for this location, try again.')
            battleship_pos()
        else:
            for i in range(size):
                x_vals.append(cor_x + 1)

def destroyer_pos():
    size = 3
    location = input('Location and orientation of your destroyer: ')
    coordinate = location.split()
    orientation = coordinate[1]
    cor_x, cor_y = coordinate[0].split()
    x_vals = [cor_x]
    if orientation == 'horizontal':
        if (cor_x + size) > 10:
            print('Ship to big for this location, try again.')
            destroyer_pos()
            
        else:
            for i in range(size):
                x_vals.append(cor_x + 1)

def submarine_pos():
    size = 3
    location = input('Location and orientation of your submarine: ')
    coordinate = location.split()
    orientation = coordinate[1]
    cor_x, cor_y = coordinate[0].split()
    x_vals = [cor_x]
    if orientation == 'horizontal':
        if (cor_x + size) > 10:
            print('Ship to big for this location, try again.')
            submarine_pos()
        else:
            for i in range(size):
                x_vals.append(cor_x + 1)

def patrol_pos():
    size = 2
    location = input('Location and orientation of your patrol ship: ')
    coordinate = location.split()
    orientation = coordinate[1]
    cor_x, cor_y = coordinate[0].split()
    x_vals = [cor_x]
    if orientation == 'horizontal':
        if (cor_x + size) > 10:
            print('Ship to big for this location, try again.')
            patrol_pos()
        else:
            for i in range(size):
                x_vals.append(cor_x + 1)
    
def something_is_still_afloat(fleet):
    pass

def ask_where_to_attack():
    pass

def get_ship_at(coordinates, fleet):
    pass

def report_hit(ship, coordinates):
    pass

def report_miss():
    pass


# You can use this game loop if you'd like
fleet = gather_fleet_positions()
while something_is_still_afloat(fleet):
    coordinates = ask_where_to_attack()
    ship = get_ship_at(coordinates, fleet)
    if ship:
        report_hit(ship, coordinates)
    else:
        report_miss()

print("The entire fleet has been sunk")

