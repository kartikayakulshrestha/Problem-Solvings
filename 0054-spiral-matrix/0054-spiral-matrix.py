class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans=[]
        n=len(matrix)
        m=len(matrix[0])
        numberOfElement=n*m
        visited=[[True]*m for i in range(n)]
        right=0
        down=m-1
        left=n-1
        up=0
        while len(ans)!=numberOfElement:
            # going right to left 
            for i in range(m):
                if visited[right][i]:
                    elem=matrix[right][i]
                    visited[right][i]=False
                    ans.append(elem)
            right+=1
            #going up to down
            for i in range(n):
                
                if visited[i][down]:
                    elem=matrix[i][down]
                    visited[i][down]=False
                    ans.append(elem)
            down-=1
            #going right to left
            for i in range(m-1,-1,-1):
                
                if visited[left][i]:
                    elem=matrix[left][i]
                    visited[left][i]=False
                    ans.append(elem)
            left-=1
            #going down to up
            for i in range(n-1,-1,-1):
                
                if visited[i][up]:
                    elem=matrix[i][up]
                    visited[i][up]=False
                    ans.append(elem)
            up+=1
        return ans
