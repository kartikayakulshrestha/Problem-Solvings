class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[None]*n for i in range(n)]
        def checkPalin(i,j):
            if i>=j:
                dp[i][j]=True
                return dp[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            if s[i]!=s[j]:
                dp[i][j]=False
                return dp[i][j]
            dp[i][j]=checkPalin(i+1,j-1)   
            return dp[i][j]
        maxi=""
        for i in range(n):
            for j in range(i,n):
                if j-i+1>len(maxi):

                    if checkPalin(i,j):
                        maxi=s[i:j+1]
        return maxi
        