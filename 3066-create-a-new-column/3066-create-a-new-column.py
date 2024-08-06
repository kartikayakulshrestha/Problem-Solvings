import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    x={"name":[],"salary":[],"bonus":[]}
    for i in range(len(employees)):
        x["name"].append(employees.name[i])
        x["salary"].append(employees.salary[i])
        x["bonus"].append(employees.salary[i]*2)
    return pandas.DataFrame(x)
    