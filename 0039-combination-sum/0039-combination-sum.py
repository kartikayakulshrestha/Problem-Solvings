class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        n=len(arr)
        dic={}
        arr.sort()
        def func(i,s,t):
            
            if t==0:
                dic[(i,t)]=[s]
                return dic[(i,t)]
            if t<0:
                dic[(i,t)]=[]
                return []
            if i>n-1:
                dic[(i,t)]=[]
                return []
        
            pick=func(i,s+[arr[i]],t-arr[i])
            nonpick=func(i+1,s,t)
            dic[(i,t)]=pick+nonpick
            return dic[(i,t)]
        
        return func(0,[],target)