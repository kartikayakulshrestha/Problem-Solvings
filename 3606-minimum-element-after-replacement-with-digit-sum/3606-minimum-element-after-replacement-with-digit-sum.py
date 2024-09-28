class Solution:
    def ss(self,n):
        x=0
        for i in str(n):
            x+=int(i)
        return x
    def minElement(self, nums: List[int]) -> int:
        c=float("inf")
        for i in nums:
            c=min(c,self.ss(i))
        return c