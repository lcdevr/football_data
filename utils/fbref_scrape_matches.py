import pandas as pd
from selectolax.parser import HTMLParser as sl
import httpx
from dataclasses import dataclass
import pyarrow

base_url = "https://fbref.com/en/matches/"
url_date = '2025-03-20'
url = f"{base_url}{url_date}"
folder_year = url_date.split('-')[0]
folder_month = url_date.split('-')[1]

r = httpx.get(url)
html = sl(r.text)

matchlist = []

for i in html.css("div.table_wrapper"):
    comp = i.css_first('h2').text()
    comp_url = i.css_first('h2 a').attributes['href']
    comp_id = i.attributes['id']
    for r in i.css('tbody tr'):
        competition = comp
        competition_url = comp_url
        competition_id = comp_id.split('_')[3]
        competition_season = comp_id.split('_')[2]
        match_date = url_date
        match_round = r.css_first('[data-stat=round]').text()
        try:
            match_week = r.css_first('[data-stat=gameweek]').text()
        except:
            match_week = None
        try:
            match_time = r.css_first('.venuetime').text()
        except:
            match_time = None
        home_team = r.css_first('[data-stat=home_team]').text()
        home_team_url = r.css_first('[data-stat=home_team] a').attributes['href']
        home_team_id = home_team_url.split('/')[3]
        match_score = r.css_first('[data-stat=score]').text()
        away_team = r.css_first('[data-stat=away_team]').text()
        away_team_url = r.css_first('[data-stat=away_team] a').attributes['href']
        away_team_id = away_team_url.split('/')[3]
        try:
            match_link_url = r.css_first('[data-stat=match_report] a').attributes['href']
        except:
            match_link_url = None
        try:
            match_id = match_link_url.split('/')[3]
        except:
            match_id = None
        attendance = r.css_first('[data-stat=attendance]').text()
        try:
            venue = r.css_first('[data-stat=venue]').text()
        except:
            venue = None
        referee = r.css_first('[data-stat=referee]').text() 
        try:
            home_team_xg = r.css_first('[data-stat=home_xg]').text()
        except:
            home_team_xg = None
        try:
            away_team_xg = r.css_first('[data-stat=away_xg]').text()
        except:
            away_team_xg = None
        notes = r.css_first('[data-stat=notes]').text()

        match = {
            'competition' : competition,
            'competition_url': competition_url,
            'competition_id': competition_id,
            'competition_season': competition_season,
            'match_date': match_date,
            'match_round': match_round,
            'match_week': match_week,
            'match_time': match_time,
            'home_team': home_team,
            'home_team_url': home_team_url,
            'home_team_id': home_team_id,
            'match_score': match_score,
            'away_team': away_team,
            'away_team_url': away_team_url,
            'away_team_id': away_team_id,
            'match_link_url': match_link_url,
            'match_id': match_id,
            'attendance': attendance,
            'venue': venue,
            'referee': referee,
            'home_team_xg': home_team_xg,
            'away_team_xg': away_team_xg,
            'notes': notes

        }

        matchlist.append(match)

df = pd.DataFrame(matchlist)
df.to_parquet(f'data\\matches\\{folder_year}\\{folder_month}\\{url_date}.parquet', engine='pyarrow', index=False)