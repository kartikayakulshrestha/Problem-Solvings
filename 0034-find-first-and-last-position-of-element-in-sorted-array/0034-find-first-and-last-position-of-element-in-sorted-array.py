class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[len(nums),-1]

        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    ans[0]=min(ans[0],mid)
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    ans[1]=max(ans[1],mid)
                l=mid+1
            else:
                r=mid-1
        if ans[0]==len(nums):
            ans[0]=-1
        
        return ans
        