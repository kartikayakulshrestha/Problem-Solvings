class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n>45:
            return []
        arr=[1,2,3,4,5,6,7,8,9]
        
        if n<9:
            arr=arr[:n]
        ans=[]
        def kartik(arr,ind,l,summ):
            
            if len(l)==k:
                if summ==n:
                    ans.append(l)
                return 
            if ind>=9 or ind>=n:
                return 
            
            pick=None
            nonPick=None
            
            if summ+arr[ind]<=n:
                pick=kartik(arr,ind+1,l+[arr[ind]],summ+arr[ind])
            
            if ind+1<=n:
                nonPick=kartik(arr,ind+1,l,summ)
            return 
              

        summ=0
        l=[]
        ind=0
        x=kartik(arr,ind,l,summ)
          
        return ans
        