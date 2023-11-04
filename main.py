from Solutions import *

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
df = createDataframe(student_data)
df2 = createDataframe(student_data)
getDataframeSize(df)

concatenateTables(df, df2)

print(df)
print(getDataframeSize(df))
