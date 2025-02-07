class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n=len(a)
        m=len(b)
        total=n+m
        half=total//2

        if m<n:
            a,b=b,a
            n,m=m,n
        
        l=0
        r=n-1
        while True:
            mid=(l+r)//2
            bmid=half-mid-2

            aleft=a[mid] if mid>=0 else float("-inf")
            aright=a[mid + 1] if mid + 1 < n else float("inf")
            bleft=b[bmid] if bmid>=0 else float("-inf")
            bright=b[bmid+1] if (bmid+1<m) else float("inf")

            if aleft<=bright and bleft<=aright:

                if total%2:
                    return min(aright,bright)
                return (max(aleft,bleft)+min(aright,bright))/2

            elif aleft>bright:
                r=mid-1
            else:
                l=mid+1