import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    x=[]
    m={
        "customer_id":[],
        "name":[],
        "email":[]
    }
    for i in range(len(customers)):
        if customers.email[i] not in m["email"]:
            m["email"].append(customers.email[i])
            m["name"].append(customers.name[i])
            m["customer_id"].append(customers.customer_id[i])
    return pandas.DataFrame(m)
            
    