class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        n=len(v)
        v.sort(key=len)
        if len(v[0])==0:
            return ""

        x=v[0]
        for i in range(1,n):
            for j in range(0,len(x)):
                if x[j]!=v[i][j]:
                    x=v[i][:j]
                    break
            if x=="":
                return ""
        return x