class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def recur(i,j,s):
            if i<0 or j<0:
                return 
            if i==0 and j==0:
                ans.append(s)
                return 
            
            recur(i-1,j,s+"(")
            if i!=j:
                recur(i,j-1,s+")")
            
                

        recur(n,n,"")
        return ans
        