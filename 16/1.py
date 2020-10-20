from typing import Dict

RANK = "rank"
NAME = "name"
COUNTRY = "country"
SCORE = "score"
BIRTH_YEAR = "birth_year"


def main():
    file_name = input('Enter filename: ')
    
    players = read_player_data_from_csv(file_name)
    show_players_by_country(players)
    show_players_by_year(players)


def read_player_data_from_csv(file_name: str) -> list:
    players = []
    with open(file_name) as file:
        for line in file:
            player_dict = parse_line(line)
            players.append(player_dict) 
    
    return players


def parse_line(line: str) -> dict:
    parts = [part.strip() for part in line.split(';')]
    return {
        RANK : int(parts[0]),
        NAME: switch_last_and_first_names(parts[1]),
        COUNTRY: parts[2],
        SCORE: int(parts[3]),
        BIRTH_YEAR: int(parts[4]),
    }    


def switch_last_and_first_names(name: str) -> str:
    last_name, first_name = name.split(',')
    return first_name.strip() + ' ' + last_name.strip()


def show_players_by_country(players) -> None:
    print('Players by country:')
    print('-------------------')
    players_by_country = group_players_by_country(players)
    sorted_countries = sorted(players_by_country.keys())
    for country in sorted_countries:
        country_players = players_by_country[country]
        show_country_stats(country, country_players)
        show_player_names_and_scores(country_players)

def show_players_by_year(players) -> None:
    print('Players by birth year:')
    print('----------------------')
    players_by_year = group_players_by_year(players)
    sorted_years = sorted(players_by_year.keys())
    for year in sorted_years:
        year_players = players_by_year[year]
        show_year_stats(year, year_players)
        show_player_names_and_scores(year_players)


def group_players_by_country(players: list) -> dict:
    grouped_players: Dict[str, list] = {}
    for player in players:
        country = player[COUNTRY]
        if country not in grouped_players:
            grouped_players[country] = []
        grouped_players[country].append(player)

    return grouped_players

def group_players_by_year(players: list) -> dict:
    grouped_players: Dict[str, list] = {}
    for player in players:
        year = player[BIRTH_YEAR]
        if year not in grouped_players:
            grouped_players[year] = []
        grouped_players[year].append(player)
    
    return grouped_players


def show_country_stats(country: str, players: list) -> None:
    average_score = calculate_average_score(players)
    print(f"{country} ({len(players)}) ({average_score:.1f}):")

def show_year_stats(year: int, players: list) -> None:
    average_score = calculate_average_score(players)
    print(f"{year} ({len(players)}) ({average_score:.1f}):")


def calculate_average_score(players: list) -> float:
    scores = [player[SCORE] for player in players]
    return sum(scores) / len(players)


def show_player_names_and_scores(players: list) -> None:
    for player in players:
        print(f"{player[NAME]:>40} {player[SCORE]:>10}")


main()
