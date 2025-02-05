class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        n=len(arr)
        ans=[]
        arr.sort()
        def func(i,s,t):
            
            if t==0:
                ans.append(s)
                return 
            if t<0:
                return 
            if i>n-1:
                return 
            
            func(i,s+[arr[i]],t-arr[i])
            func(i+1,s,t)
        func(0,[],target)
        return ans