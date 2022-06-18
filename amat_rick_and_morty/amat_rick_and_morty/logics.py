import pandas as pd
from typing import Dict, List


def compare_two_characters(char_1: Dict[str, str], char_2: Dict[str, str]) -> Dict[str, bool]:
    return {k: char_2[k] == prop_1 for k, prop_1 in char_1.items()}


def get_compare_two_characters_df(char_1: Dict[str, str], char_2: Dict[str, str], ak: List[str]) -> pd.DataFrame:
    _compare = {k: [char_2[k], char_1[k]] for k, v in char_1.items() if k in ak}
    return pd.DataFrame(_compare)
