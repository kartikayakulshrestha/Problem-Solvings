class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        blank=n
        curr=n
        flag=0
        for i in range(n-1,-1,-1):
            if s[i]==" ":
                if flag:
                    
                    return blank-i-1
                blank=i
            else:
                flag=1 
        return blank-i