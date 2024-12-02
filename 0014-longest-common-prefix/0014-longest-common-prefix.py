class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        strs=""
        v.sort(key=len)
        flag=0
        mini=v[0]
        m=len(mini)
        n=len(v)
        if n==1:
            return v[0]
        for i in range(m):
            x=v[0][i]
            for j in range(n):
                if v[j][i]!=x:
                    flag=1
                    break
            
            if flag:
                return strs

            strs+=x
        
        return strs