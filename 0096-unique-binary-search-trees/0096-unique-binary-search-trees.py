class Solution:
    def numTrees(self, n: int) -> int:
        def fact(i):
            x=1
            for i in range(1,i+1):
                x*=i
            return x
        
        return fact(2*n)//(fact(n+1)*fact(n))
        