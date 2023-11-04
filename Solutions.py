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


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students = students[students["student_id"] == 101].drop("student_id", axis=1)
    return students


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email')
    return customers


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset='name')
    return students
