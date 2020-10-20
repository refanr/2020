RANK = "rank"
NAME = "name"
COUNTRY = "country"
SCORE = "score"
BIRTH_YEAR = "birth_year"


def main():
    #file_name = input('Enter filename: ')
    file_name = '/Users/refan/python/Forritun/2020/16/1.csv'
    players = read_player_data_from_csv(file_name)
    show_players_by_country(players)

def read_player_data_from_csv(file_name: str) -> list:
    players = []
    with open(file_name) as file:
        for line in file:
            player_dict = parse_line(line)
            players.append(player_dict) 
    
    return player_dict
    
def parse_line(line: str) -> dict:
    parts = line.split('; ')
    return {
        RANK : int(parts[0]),
        NAME: switch_last_and_first_names(parts[1]),
        COUNTRY: parts[2],
        SCORE: int(parts[3]),
        BIRTH_YEAR: int(parts[4]),
    }    

def switch_last_and_first_names(name: str) -> str:
    last_name, first_name = name.split(', ')
    return f"{first_name} {last_name}" 

def show_players_by_country(players):
    pass

main()
