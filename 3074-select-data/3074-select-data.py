import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    x={
        "name":[],
        "age":[]
    }
    for i in range(len(students)):
        if students.student_id[i]==101:
            return pandas.DataFrame({"name":[students.name[i]],"age":[students.age[i]]})
    return pandas.DataFrame({"name":[],"age":[]})