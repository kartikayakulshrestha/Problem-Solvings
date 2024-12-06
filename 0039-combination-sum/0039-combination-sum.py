class Solution:
    def combinationSum(self, arr: List[int], t: int) -> List[List[int]]:
        l=[]
        p=[]
        dic={}
        def ram(arr,t,n,l):
            if (n,t) in dic:
                return  
            
            if t==0:
                p.append(l)
                return None
            pick=None
            notpick=None
            if (n,t) in dic:
                return dic[(n,t)]
            if t-arr[n]>=0:
                pick=ram(arr,t-arr[n],n,l+[arr[n]])
            if n!=0:
                nonpick=ram(arr,t,n-1,l)
                
            if pick and notpick:
                dic[(n,t)]=[pick,notpick]
            elif pick:
                dic[(n,t)]=pick
            elif notpick:
                dic[(n,t)]=notpick
            else:
                return None
            
            
            return 
        n=len(arr)-1
        x=ram(arr,t,n,l)
        return p
        