class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ar={}
        for i in arr:
            if i not in ar:
                ar[i]=1
            else:
                ar[i]=0
        x=[]
        for i,j in ar.items():
            if j!=0:
                x.append([i,j])
        if len(x)<k:
            return ""

        return x[k-1][0]
        
            