""" open the csv file, read the file, line by line and make some data struct 
for each line, each player. 

"""

def main():
    file_name = input('Enter filename: ')
    players = read_player_data_from_csv(file_name)
    show_players_by_country(players)

def read_player_data_from_csv(file_name: str):
    return []

def show_players_by_country(players):
    pass

main()
