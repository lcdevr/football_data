def scrape_results():
    # Scrape the results of the matches
    pass

def scrape_matches():
    # Scrape the matches
    pass

def scrape_players():
    # Scrape the players
    pass


def main():
    # Defining what to scrape
    scrape_choice = input('What do you want to scrape? (1) - Comp Fixtures and Results, (2) - Matches, (3) - Player, (4) - Other: ')
    if scrape_choice == '1':
        print('Scraping Comp Fixtures and Results...')
        scrape_results()
    elif scrape_choice == '2':
        print('Scraping Matches...')
        scrape_matches()
    elif scrape_choice == '3':
        print('Scraping Players...')
        scrape_players()
    elif scrape_choice == '4':
        print('Scraping Other...')
    else:
        print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()