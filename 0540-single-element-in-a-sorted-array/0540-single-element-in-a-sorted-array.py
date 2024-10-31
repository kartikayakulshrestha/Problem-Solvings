class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return arr[0]
        if n==3:
            if arr[0]==arr[1]:
                return arr[2]
            else:
                return arr[0]
        if arr[0]!=arr[1]:
            return arr[0]
        elif arr[n-1]!=arr[n-2]:
            return arr[n-1]
        
        l=1
        r=n-2
        mid=l+(r-l)//2
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid] ==arr[mid-1]:
                if mid%2:
                    l=mid+1
                else:
                    r=mid-1
            elif arr[mid]==arr[mid+1]:
                if mid%2:
                    r=mid-1
                else:
                    l=mid+1
            else:
                return arr[mid]
       