import pandas as pd
<<<<<<< HEAD

def build_league_lookup():
    comp_url = 'https://fbref.com/en/comps/'
    tbl_nos = [2,3,4,5]
    for table in tbl_nos:
        comps = pd.read_html(comp_url,extract_links ='body')[table]
        comp_list = comps[['Competition Name','Country', 'Gender','Last Season']].values.tolist()
        teams =  []
        country = []
        gender = []
        season_url = []
        for comp in comp_list:
            teams.append(comp[0][0])
            country.append(comp[1][0])
            gender.append(comp[2][0])
            season_url.append('https://fbref.com' + comp[3][1])

        leagues = pd.DataFrame({'League':teams, 'Country':country, 'Gender':gender, 'Season Url':season_url})
        leaguelist.append(leagues)



def build_team_lookup():
    pass



def main():
    build_league_lookup()
=======
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
>>>>>>> 42db29b2e64cdbdcfdc376eb210e1be6f938637c

if __name__ == '__main__':
    main()