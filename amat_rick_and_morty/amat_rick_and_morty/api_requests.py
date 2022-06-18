from requests import request
from typing import (
    Dict
)

API_HOME_URL = "https://rickandmortyapi.com/api"


def get_character_data_by_name(name: str, data_key: str = 'results') -> Dict[str, str]:
    try:
        return request(url=API_HOME_URL + "/character",
                       method='GET',
                       params={'name': name}).json()[data_key][0]
    except KeyError:
        pass
    return {}
