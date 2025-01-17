class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        n=len(s)
        r=n-1
        def check(ss,s1):
            return ss==s1
        left=""
        right=""
        flag=1
        while l<=r:
            if s[l]!=s[r]:
                if flag:
                    flag=0
                    l+=1
            left+=s[l]
            right+=s[r]
            l+=1
            r-=1
        t1=check(left,right)
        
        left=""
        right=""
        l=0
        r=n-1
        flag=1
        while l<=r:
            if s[l]!=s[r]:
                if flag:
                    flag=0
                    r-=1
                
            left+=s[l]
            right+=s[r]
            l+=1
            r-=1
        
        t2=check(left,right)
        
        return t1 or t2
