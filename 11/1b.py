import string
upps = string.ascii_uppercase

SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)

 
# ... add your functions here
def gather_fleet_positions():
    print('Specify the location of each ship in your fleet by providing the top/left coordinate and orientation.')
    print("Examples: 'A2 vertical' or 'C3 horizontal'")
    carrier = input('Location and orientation of your carrier: ').split()
    battleship = input('Location and orientation of your battleship: ').split()
    destroyer = input('Location and orientation of your destroyer: ').split()
    submarine = input('Location and orientation of your submarine: ').split()
    patrol_boat = input('Location and orientation of your patrol boat: ').split()
    return carrier, battleship, destroyer, submarine, patrol_boat
    
    

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
print(fleet)
