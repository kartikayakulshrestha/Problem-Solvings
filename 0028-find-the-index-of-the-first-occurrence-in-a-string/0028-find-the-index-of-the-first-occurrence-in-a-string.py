class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index=0
        m=len(needle)
        n=len(haystack)
        if n<m:
            return -1
        if n==m:
            return 0 if haystack==needle else -1
        for i in range(n):
            if haystack[i]==needle[0]:
                
                flag=1
                for j in range(m):
                    if i+j>=n:
                        flag=0
                        break
                    if haystack[i+j]!=needle[j]:
                        flag=0
                        break
                if flag:
                    return i
        return -1