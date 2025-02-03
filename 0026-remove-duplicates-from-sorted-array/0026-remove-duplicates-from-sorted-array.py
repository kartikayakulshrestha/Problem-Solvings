class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=set()
        j=0
        for i in range(len(nums)):
            if nums[i] not in x:
                x.add(nums[i])
                nums[j]=nums[i]
                j+=1
        return len(x)