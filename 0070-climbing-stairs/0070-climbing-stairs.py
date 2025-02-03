class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def func(step):
            
            if step<2:
                return 1
            if dp[step]>0:
                return dp[step]
            dp[step]=func(step-1)+func(step-2)
            return dp[step]

        return func(n)
        