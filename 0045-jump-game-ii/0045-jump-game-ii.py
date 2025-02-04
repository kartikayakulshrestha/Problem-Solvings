class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        dp=[float('inf')]*n
        dp[0]=0
        for i in range(n):
           for j in range(i+1,min(nums[i]+i+1,n)): 
                dp[j]=min(dp[i]+1,dp[j])
        
        return dp[-1]