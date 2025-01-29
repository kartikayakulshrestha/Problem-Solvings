class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        lmax=0
        rmax=0
        l=0
        r=n-1
        ans=0
        while l<=r:
            lmax=max(arr[l],lmax)
            rmax=max(arr[r],rmax)
            if arr[l]<=arr[r]:
                ans+=min(lmax,rmax)-arr[l]
                
                l+=1
            else:
                ans+=min(lmax,rmax)-arr[r]
                
                r-=1
        return ans
            