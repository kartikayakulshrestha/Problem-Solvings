class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        t=[-1]*(n-1)
        left,right=[arr[0]]+t,t+[arr[-1]]
        for i in range(1,n):
            left[i]=max(left[i-1],arr[i])
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],arr[i])

        add=0
        
        for i in range(1,n-1):
            add+=min(left[i],right[i])-arr[i]
        return add 