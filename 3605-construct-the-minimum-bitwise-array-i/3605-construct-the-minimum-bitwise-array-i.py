class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            flag=-1
            for j in range(1,nums[i]):
                if j|j+1 == nums[i]:
                    flag=j
                    break
            ans.append(flag)
        return ans
        