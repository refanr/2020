RANK = "rank"
NAME = "name"
COUNTRY = "country"
SCORE = "score"
BIRTH_YEAR = "birth_year"

def main():
    file_name = input('Enter filename: ')
    players = read_player_data_from_csv(file_name)
    show_players_by_country(players)

def read_player_data_from_csv(file_name: str):
    players = []
    with open(file_name) as file:
        for line in file:
            player_dict = parse_line(line) 
    
    return player_dict
    
    

def show_players_by_country(players):
    pass

main()
