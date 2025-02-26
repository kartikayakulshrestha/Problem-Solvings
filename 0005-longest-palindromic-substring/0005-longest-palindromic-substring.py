class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[-1]*len(s) for i in range(len(s))]
        def checkPalin(i,j):
            if i>=j:
                return True
            if s[i]!=s[j]:
                dp[i][j]=False
                return dp[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=checkPalin(i+1,j-1)
                return dp[i][j]
        maxlen=0
        starting=0
        for i in range(len(s)):
            for j in range(len(s)-1,i-1,-1):
                if checkPalin(i,j):
                    if j-i+1>maxlen:
                        maxlen=j-i+1
                        starting=i
        return s[starting:starting+maxlen]
        