import requests
import pytest

API_URL = "http://localhost:5000"
result = ["The surname 'Nowak' is in position 1 and is held by 99803 people.",
          "The surname 'Kowalski' is in position 2 and is held by 67505 people.",
          "The surname 'Żmuda-Trzebiatowska' is in position 14636 and is held by 225 people."
          "The surname 'Abdulsalam A.Ebrahim' is in position 273992 and is held by 2 people.",
          "No information found for the surname 'Asdf'."]


@pytest.mark.parametrize(
        "gender,surname,result", [('F', 'Nowak', result[0]),
                                  ('m', 'Kowalski', result[1]),
                                  ('k', 'Żmuda-Trzebiatowska', result[2]),
                                  ('M', 'ABDULSALAM A.EBRAHIM', result[3]),
                                  ('M', 'asdf', result[4])])
def test_bot_add_normal_data(gender, surname, result):
    body = {
        'gender': gender,
        'surname': surname
    }
    response = requests.post(f"{API_URL}/surname", json=body)
    print(response.status_code)
    print(response.json())
    assert response.json()["result"] == result, "WRONG RESULT"