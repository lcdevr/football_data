import pandas as pd

def main():
    comp_url = 'https://fbref.com/en/comps/'
    comps = pd.read_html(comp_url,extract_links ='body')
    print(comps)

if __name__ == '__main__':
    main()