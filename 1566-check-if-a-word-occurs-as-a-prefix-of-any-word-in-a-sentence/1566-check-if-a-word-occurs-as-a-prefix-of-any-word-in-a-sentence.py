class Solution:
    def isPrefixOfWord(self, arr: str, s: str) -> int:
        l=arr.split()
        n=len(s)
        for i in range(len(l)):
            c=0
            
            if len(l[i])>=n:
                
                for j in range(n):
                    
                    if s[j]==l[i][j]:
                        c+=1

            if c==n:
                return i+1
        return -1
        