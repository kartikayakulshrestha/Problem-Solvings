class Solution:
    def searchInsert(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        ans=0
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==val:
                return mid
            if nums[mid]<val:
                ans=max(mid+1,ans)
                l=mid+1
            else:
                r=mid-1
        return ans