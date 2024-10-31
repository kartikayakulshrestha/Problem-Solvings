class Solution:
    def findMin(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        ans=float("inf")
        if len(arr)==1 or len(arr)==2:
            return min(arr)

        while l<=r:
            mid=l+(r-l)//2
            
            if arr[mid]>=arr[l]:
                ans=min(arr[l],ans)
                l=mid+1
            elif arr[mid]<=arr[r]:
                ans=min(arr[mid],ans)
                r=mid-1
        
        return ans