import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    c=0
    for i in players:
        c+=1
    return [len(players),c]