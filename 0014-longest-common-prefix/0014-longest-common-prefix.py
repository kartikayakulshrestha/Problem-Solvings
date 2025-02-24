class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        x=strs[0]
        n=len(strs)
        for i in range(0,n):
            for j in range(min(len(x),len(strs[i]))):
                if strs[i][j]!=x[j]:
                    x=strs[i][:j]
                    break
        return x