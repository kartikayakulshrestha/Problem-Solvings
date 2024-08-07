class Solution:
    
    def rob(self, nums: List[int]) -> int:
        dp=[0 for i in range(len(nums))]
        arr=nums
        dp[0]=0
        for i in range(len(nums)):
            if i==0:
                dp[i]=arr[i]
            elif i-2>=0:
                left=dp[i-2]+arr[i]
                right=dp[i-1]
                dp[i]=max(left,right)
            elif i-2==-1:
                left=arr[i]
                right=dp[i-1]
                dp[i]=max(left,right)
        return dp[-1]