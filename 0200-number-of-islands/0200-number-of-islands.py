class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        visted=[[False]*m for i in range(n)]
        count=0
        def findpath(i,j):
            if i+1<n and (visted[i+1][j]==False and grid[i+1][j]=="1"):
                visted[i+1][j]=True
                findpath(i+1,j)
            if i-1>=0 and (visted[i-1][j]==False and grid[i-1][j]=="1"):
                visted[i-1][j]=True
                findpath(i-1,j)
            if j+1<m and (visted[i][j+1]==False and grid[i][j+1]=="1"):
                visted[i][j+1]=True
                findpath(i,j+1)
            if j-1>=0 and (visted[i][j-1]==False and grid[i][j-1]=="1"):
                visted[i][j-1]=True
                findpath(i,j-1)
            return 
            
            

        countIsland=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visted[i][j]==False:
                    
                    findpath(i,j)
                    
                    countIsland+=1
        return countIsland
        