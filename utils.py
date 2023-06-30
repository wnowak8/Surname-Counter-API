import pandas as pd

FEMALE_URL = r'https://api.dane.gov.pl/media/resources/20230131/' + \
    r'nazwiska_%C5%BCe%C5%84skie-osoby_%C5%BCyj%C4%85ce.csv'
MALE_URL = r'https://api.dane.gov.pl/media/resources/20230131/' + \
    r'nazwiska_m%C4%99skie-osoby_%C5%BCyj%C4%85ce.csv'


def get_info(url: str, surname: str) -> str:
    """
    Retrieves information about the given surname.

    Args:
        url (str): The URL address of the CSV file containing the surname data.
        surname (str): The surname to search for.

    Returns:
        str: Information about the given surname as text.

    Raises:
        IndexError: If the specified surname is not found in the data.

    """
    df = pd.read_csv(url)
    df.index = range(1, len(df)+1)
    surname = surname.lower()
    df["Nazwisko aktualne"] = df["Nazwisko aktualne"].str.lower()
    try:
        surname_index = df.loc[df['Nazwisko aktualne'] == surname].index[0]
        surname_count = df['Liczba'][surname_index]
        surname = '-'.join(word.title() for word in surname.split('-'))
        response = f"The surname '{surname.title()}' is in position " + \
            f"{surname_index} and is held by {surname_count} people."
    except IndexError:
        response = f"No information found for the surname '{surname.title()}'."

    return response


def get_surname_info(gender: str, surname: str) -> str:
    """
    Retrieves information about the given surname and gender.

    Args:
        gender (str): The gender ('F' - female, 'M' - male).
        surname (str): The surname to search for.

    Returns:
        str: Information about the given surname and gender as text.

    """
    if gender.upper() == 'F':
        return get_info(url=FEMALE_URL, surname=surname)
    elif gender.upper() == 'M':
        return get_info(url=MALE_URL, surname=surname)
