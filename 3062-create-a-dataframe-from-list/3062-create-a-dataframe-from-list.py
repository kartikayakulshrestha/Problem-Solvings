import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    x={
        "student_id":[],
        "age":[]
    }
    for i,j in student_data:
        x["student_id"].append(i)
        x["age"].append(j)
    return pandas.DataFrame(x)
    