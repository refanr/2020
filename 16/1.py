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

def show_players_by_country(players) -> None:
    print('Players by country:')
    print('-------------------')
    players_by_country = group_players_by_country(players)
    sorted_countries = sorted(players_by_country.keys())
    for country in sorted_countries:
        country_players = players_by_country[country]
        show_country_stats(country, players_by_country)
        show_player_names_and_scores(country_players)

def group_players_by_country(players: list) -> dict:
    return {}

def show_country_stats(country: str, players: list) -> None:
    pass

def show_player_names_and_scores(players: list) -> None:
    pass

main()
