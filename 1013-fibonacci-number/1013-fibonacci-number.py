class Solution:
    def fib(self, n: int) -> int:
        n1,n2=0,1
        summ=0
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                summ=n1+n2
                n1=n2
                n2=summ
            return summ