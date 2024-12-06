class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        l=[]
        
        def palind(s):
          return s==s[::-1]
        def kartik(s,n,l):
            
            if n==x:
               
               ans.append(l)
               return 
            
            for i in range(n+1,x+1):
                p=s[n:i]
                
                if p==p[::-1]:
                    
                    pick=kartik(s,i,l+[p])
            
            
            
            return 
            
        n=0
        x=len(s)
        p=kartik(s,n,l)
        return ans