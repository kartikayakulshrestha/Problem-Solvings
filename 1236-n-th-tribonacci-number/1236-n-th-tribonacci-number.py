class Solution:
    def tribonacci(self, n: int) -> int:
        
        x_0=0
        x_1=1
        x_2=1
        print(n==0)
        if n==0:
            return 0
        else:
            for i in range(2,n):
                x=x_0+x_1+x_2
                x_0=x_1
                x_1=x_2
            
                x_2=x
            
            return x_2