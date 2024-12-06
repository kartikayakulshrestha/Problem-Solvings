class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        dic={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans=[]
        s=""
        if d=="":
            return []

        def kartik(d,ind,l):
            if ind==n:
                ans.append(l)
                return 
            for i in dic[d[ind]]:
                pick=kartik(d,ind+1,l+i)
            return 
        n=len(d)
        ind=0
        l=""
        x=kartik(d,ind,l)
        ans.sort()
        return ans

        