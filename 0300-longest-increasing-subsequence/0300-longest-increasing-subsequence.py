class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)] 
        for index in range(n - 1, -1, -1):  # Iterate from right to left
            for prev in range(index - 1, -2, -1):  # Previous index (-1 for no previous)
                # Option 1: Skip current element
                nonpick = dp[index + 1][prev + 1]

                # Option 2: Pick current element if valid
                pick = 0
                if prev == -1 or nums[prev] < nums[index]:
                    pick = 1 + dp[index + 1][index + 1]

                dp[index][prev + 1] = max(pick, nonpick)

        return dp[0][0]
       
        
        