class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def recur(m):
            if m==2:
                return 2
            if m==1:
                return 1
            if dp[m]!=-1:
                return dp[m]
            dp[m]=recur(m-1)+recur(m-2)
            return dp[m]

        return recur(n)      