class Solution:
    def minimumSteps(self, s: str) -> int:
        c=0
        l=[]
        for i in range(len(s)):
            if s[i]=="0":
                c+=1
                l.append(i)
    
        x=0
        for i in range(len(l)):
            x+=(l[i]-i)
            
        return x
