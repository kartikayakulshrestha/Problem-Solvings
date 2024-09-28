class Solution:
    def maximumTotalSum(self, arr: List[int]) -> int:
        arr.sort()
        curr=arr[-1]
        t=0
        for i in range(len(arr)-1,-1,-1):
            curr=min(curr,arr[i])

            if curr<=0:
                return -1
            t+=curr
            curr-=1
        return t