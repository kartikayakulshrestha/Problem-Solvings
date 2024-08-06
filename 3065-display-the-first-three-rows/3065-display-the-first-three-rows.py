import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:

    if len(employees)>2:
        c={"employee_id":[],"name":[],"department":[],"salary":[]}
        for i in range(3):
            c["employee_id"].append(employees["employee_id"][i])
            c["name"].append(employees["name"][i])
            c["department"].append(employees["department"][i])
            c["salary"].append(employees["salary"][i])
        return pandas.DataFrame(c)
    else:
        c={"employee_id":[],"name":[],"department":[],"salary":[]}
        for i in range(len(employees)):
            c["employee_id"].append(employees["employee_id"][i])
            c["name"].append(employees["name"][i])
            c["department"].append(employees["department"][i])
            c["salary"].append(employees["salary"][i])
        return pandas.DataFrame(c)