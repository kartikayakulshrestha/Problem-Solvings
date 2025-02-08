class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        ans=float("-inf")
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid<=x:
                ans=max(mid,ans)
                l=mid+1
            else:
                r=mid-1
        return ans
        