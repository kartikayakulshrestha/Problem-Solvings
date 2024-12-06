class Solution:
    def combinationSum2(self, arr, t):
        #your code goes here
        l=[]
        p=[]
        
        def ram(arr,t,n,l):
             
            if t==0:
                for i in p:
                    if l==i:
                        return
                
                p.append(l)
                return 
            if n<0:
                return
            pick=None
            nopick=None
            if t-arr[n]>=0:
                pick=ram(arr,t-arr[n],n-1,l+[arr[n]])
            if n>=0:
                
                while n>=0 and arr[n] in l:
                    
                    n-=1
                notpick=ram(arr,t,n-1,l)
            
            
            return 
        n=len(arr)-1
        x=sorted(arr)[::-1]
        ram(x,t,n,l)
        return p