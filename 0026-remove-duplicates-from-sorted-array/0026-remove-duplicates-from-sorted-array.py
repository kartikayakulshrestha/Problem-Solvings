class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=list(set(nums))
        index=0
        x.sort()
        for i in x:
            nums[index]=i
            index+=1
        return len(x)