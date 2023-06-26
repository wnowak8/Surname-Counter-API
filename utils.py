import pandas as pd

FEMALE_URL = r'https://api.dane.gov.pl/media/resources/20230131/nazwiska_%C5%BCe%C5%84skie-osoby_%C5%BCyj%C4%85ce.csv'
MALE_URL = r'https://api.dane.gov.pl/media/resources/20230131/nazwiska_m%C4%99skie-osoby_%C5%BCyj%C4%85ce.csv'


def get_info(url: str, surname: str):
    df = pd.read_csv(url)
    df.index = range(1, len(df)+1)
    surname = surname.lower()
    df["Nazwisko aktualne"] = df["Nazwisko aktualne"].str.lower()
    surname_index = df.loc[df['Nazwisko aktualne'] == surname].index[0]
    surname_count = df['Liczba'][surname_index]
    surname = '-'.join(word.title() for word in surname.split('-'))
    response = f"The surname '{surname.title()}' is in position {surname_index} and is held by {surname_count} people."
    return response


def get_surname_info(gender: str, surname: str):
    if gender.upper() == 'F':
        return get_info(url=FEMALE_URL, surname=surname)
    elif gender.upper() == 'M':
        return get_info(url=MALE_URL, surname=surname)
