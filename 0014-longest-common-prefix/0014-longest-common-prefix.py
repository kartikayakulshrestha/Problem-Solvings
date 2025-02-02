class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        n=len(v)
        v.sort()
        
        first=v[0]
        last=v[-1]
        a=""
        for i in range(0,min(len(first),len(last))):
            if first[i]!=last[i]:
                return a
            a+=first[i]
        return a