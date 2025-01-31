class Solution:
    def longestPalindrome(self, s: str) -> str:
        #because we are going through all of the substrings
        

        dp=[[-1]*len(s) for i in range(len(s))]
        def solve(i,j):
            if dp[i][j]==1 or dp[i][j]==0:
                return dp[i][j]
            if i>=j:
                dp[i][j]=True
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=solve(i+1,j-1)
                return dp[i][j]
            else:
                dp[i][j]=False
                return dp[i][j]
        startpoint=-1
        leng=0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if solve(i,j):
                    
                    if leng<j-i+1:
                        leng=j-i+1
                        startpoint=i
        return s[startpoint:leng+startpoint]