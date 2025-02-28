class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxsum=currsum=nums[0]

        for i in nums[1:]:
            currsum=max(currsum+i,i)
            maxsum=max(currsum,maxsum)
        return maxsum
        