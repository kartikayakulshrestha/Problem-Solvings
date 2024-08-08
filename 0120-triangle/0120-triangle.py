class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        arr=triangle
        dp=[[0 for i in range(j+1)] for j in range(len(arr))]
        
        for i in range(len(arr)-1,-1,-1):
            for j in range(i+1):
                if i == len(arr)-1:
                    dp[i][j]=arr[i][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+arr[i][j]
        
        return dp[0][0]