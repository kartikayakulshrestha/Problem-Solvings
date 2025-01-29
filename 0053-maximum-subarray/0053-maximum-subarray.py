class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum=maximumSum=nums[0]

        for i in range(1,len(nums)):
            currentSum=max(nums[i],currentSum+nums[i])
            maximumSum=max(currentSum,maximumSum)
        return maximumSum
        
            