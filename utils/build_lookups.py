import pandas as pd
import time
import csv

def build_team_lookup():
    squads = pd.read_html('https://fbref.com/en/squads/', extract_links='body', match='Countries')[0]
    squads = squads.head(1)
    squads = squads['Country']
    team_list = []
    team = []
    for squad in squads:
        time.sleep(7.5)
        country = squad[0].replace(' Football Clubs', '')
        s = squad[1]
        url = f'https://fbref.com{s}'
        dfs = pd.read_html(url, match='Squad', header=0)[0]
        for row in dfs.iterrows():
#           print(row[1]['Squad'], country)
           teamcountry = [x for x in (row[1]['Squad'],row[1]['Gender'] ,country)]
           apend = team.append(teamcountry)
    
    return team

def write_team_lookup(teamlist):
    with open('data\\lookups\\teams.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(teamlist)


def build_league_lookup():
    pass

def main():
    teamlist = build_team_lookup()
    write_team_lookup(teamlist)

if __name__ == '__main__':
    main()