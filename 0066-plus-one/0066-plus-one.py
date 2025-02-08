class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        x=0
        for i in range(n):
            x=x*10+digits[i]
        
        return list(map(int,str(x+1)))
        