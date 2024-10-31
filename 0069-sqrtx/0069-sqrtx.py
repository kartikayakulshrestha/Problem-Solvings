class Solution:
    def mySqrt(self, n: int) -> int:
        l=0
        r=n
        mid=l+(r-l)//2
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid ==n:
                return mid
            elif mid*mid>n:
                r=mid-1

            else:
                ans=max(ans,mid)
                l=mid+1
        return ans
                