import pandas as pd

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

if __name__ == '__main__':
    main()