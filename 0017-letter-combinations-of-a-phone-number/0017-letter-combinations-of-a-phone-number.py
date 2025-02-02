class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={
            2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"
        }
        n=len(digits)
        def recur(i,s):
            if i==n:
                return [s]
            l=[]
            for index in dic[int(digits[i])]:
                l+=recur(i+1,s+index)
            return l
        if digits=="":
            return []
        return recur(0,"")