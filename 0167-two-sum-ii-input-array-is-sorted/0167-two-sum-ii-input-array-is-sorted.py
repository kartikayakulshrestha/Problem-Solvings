class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        
        n=len(arr)
        l=0
        r=n-1
        while l<=r:
            x=arr[l]+arr[r]
            if x==target:
                return [l+1,r+1]
            elif x>target:
                r-=1
            else:
                l+=1
        
