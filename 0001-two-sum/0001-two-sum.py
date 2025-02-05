class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        n=len(nums)
        for i in range(n):
            x=target-nums[i]
            if nums[i] in dic:
                return [dic[nums[i]],i]
            dic[x]=i
        
        