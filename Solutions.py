from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    columns = len(players.columns)
    rows = len(players)
    return [rows, columns]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[0:3]
