class Solution:
    
    def climbStairs(self, n: int) -> int:
        dic={1:1,2:2}
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(3,n+1):
            dic[i]=dic[i-2]+dic[i-1]
        return dic[n]
        

        