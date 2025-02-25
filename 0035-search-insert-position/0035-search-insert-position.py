class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,e in enumerate(nums):
            if target<=e:
                return i
        return len(nums)
        