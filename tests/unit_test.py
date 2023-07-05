import pytest
import context
from service import get_surname_info


result = ["The surname 'Nowak' is in position 1 and is held by 101512 people.",
          "The surname 'Kowalski' is in position 2 and is held by 67505 people.",
          "The surname 'Zmuda-Trzebiatowska' is in position 43273 and is held by 61 people.",
          "The surname 'Abdulsalam A.Ebrahim' is in position 273992 and is held by 2 people.",
          "No information found for the surname 'Asdf'."]


@pytest.mark.parametrize(
        "gender,surname,result", [('F', 'Nowak', result[0]),
                                  ('m', 'Kowalski', result[1]),
                                  ('f', 'Zmuda-Trzebiatowska', result[2]),
                                  ('M', 'ABDULSALAM A.EBRAHIM', result[3]),
                                  ('M', 'asdf', result[4])])
def test_get_surname_info(gender, surname, result):
    _result = get_surname_info(gender=gender, surname=surname)
    assert _result == result, "WRONG RESULT"
