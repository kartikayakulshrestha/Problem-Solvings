class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort(key=lambda x:x[0])
        ans=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            if ans[-1][1]>=nums[i][0]:
                ans[-1][1]=max(nums[i][1],ans[-1][1])
            else:
                ans.append(nums[i])
        return ans