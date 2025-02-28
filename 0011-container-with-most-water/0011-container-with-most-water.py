class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l=0
        n=len(arr)
        r=n-1
        maxArea=0
        while l<r:
            maxArea=max(min(arr[l],arr[r])*(r-l),maxArea)
            if arr[l]<=arr[r]:
                l+=1
            else:
                r-=1
        return maxArea
        