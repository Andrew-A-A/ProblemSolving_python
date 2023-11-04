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


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={"id": "student_id",
                                        'first': 'first_name',
                                        'last': 'last_name',
                                        'age': 'age_in_years'})
    return students


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1._append(df2)


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    h = animals[animals['weight'] > 100]
    h = h.sort_values(by='weight',ascending=False)
    return h[['name']]
