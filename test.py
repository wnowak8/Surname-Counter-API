import requests


def test(gender: str, surname: str) -> dict:
    """
    Sends a POST request to the specified URL to retrieve information about
    a surname.

    Args:
        gender (str): The gender ('F' - female, 'M' - male).
        surname (str): The surname to search for.

    Returns:
        dict: A dictionary containing the response data from the API.
            If the request is successful, the dictionary will contain the
            retrieved information.
            If the request encounters an error or the surname information is
            not found, the dictionary will contain a 'result' key with
            a corresponding informative message.

    """
    url = 'http://127.0.0.1:5000/surname'
    headers = {'Content-Type': 'application/json'}
    data = {
        'gender': gender,
        'surname': surname
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"JSON decoding error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return {'result': f"No information found for the surname '{surname}'."}


test_male_surname = ['asdf', 'Nowak', 'Kłak', 'ABDULSALAM A.EBRAHIM',
                     'DR. VARGA', 'M.A.SALAM', 'K.C.']
for surname in test_male_surname:
    result = test(gender='m', surname=surname)
    print(f"Test for male surname '{surname}':")
    if 'result' in result:
        print(result['result'])
    else:
        print("Unexpected response:", result)
    print('-' * 80)

test_female_surname = ['Nowak', 'Żmuda-Trzebiatowska', 'ABDULSALAM A.EBRAHIM',
                       'DR. VARGA', 'M.A.SALAM', 'K.C.']
for surname in test_female_surname:
    result = test(gender='f', surname=surname)
    print(f"Test for female surname '{surname}':")
    if 'result' in result:
        print(result['result'])
    else:
        print("Unexpected response:", result)
    print('-' * 80)
