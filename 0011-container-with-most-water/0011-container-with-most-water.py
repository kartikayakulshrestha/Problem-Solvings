class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lmax=0
        rmax=0
        ans=0
        while i<=j:
            ans=max(ans,min(height[i],height[j])*(j-i))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return ans
        